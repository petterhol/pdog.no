#!/usr/bin/env python3
"""Synkroniserer MindNode-kartet «Ryddedagen» med innholdet i content/.

Bruk:
    python3 tools/ryddesynk.py kart.txt            # rapport, endrer ingenting
    python3 tools/ryddesynk.py kart.txt --apply    # utfører endringene i content/

kart.txt er eksporten fra MindNode i formatet «indented-list», hentet via
MindNode-MCP-en (mindnode://documents/<id>/content/indented-list).

Regler:
  * En node er en side hvis den ligger på nivå 2, eller hvis den har en lenke
    til ryddedagen.no. Dypere noder uten slik lenke er innhold på siden over.
  * Lenken er identiteten. Derfor kjennes omdøping igjen som omdøping.
  * Rekkefølgen i kartet blir weight. Seksjon blir nodens øverste forelder.
  * Tekst i sidene røres aldri. Sletting skjer aldri. Titler overskrives ikke,
    bare rapporteres.
  * Sider i roten av content/ (om, personvern, kontakt ...) holdes utenfor.
"""
import json, os, re, sys, unicodedata

# Lenken på noden er identiteten. Basen kan byttes uten at identiteten ryker:
# alle basene under gjenkjennes ved lesing, og SKRIV_BASE brukes på nye lenker.
BASER = ("http://localhost:1313", "https://ryddedagen.no")
SKRIV_BASE = BASER[0]
BASE = SKRIV_BASE
ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROT, "content")


def slugify(tittel):
    t = tittel.lower()
    for a, b in (("æ", "ae"), ("ø", "o"), ("å", "a")):
        t = t.replace(a, b)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "side"


def les_unntak():
    """Nodetitler som aldri skal bli egne sider."""
    sti = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ryddesynk-unntak.txt")
    if not os.path.exists(sti):
        return set()
    ut = set()
    for linje in open(sti, encoding="utf-8"):
        linje = linje.strip()
        if linje and not linje.startswith("#"):
            ut.add(linje)
    return ut


def les_kart(sti):
    """-> liste av (nivå, tittel, lenke|None) i dokumentrekkefølge."""
    noder = []
    for linje in open(sti, encoding="utf-8").read().split("\n"):
        if not linje.strip():
            continue
        if linje.startswith("\t"):
            niva = len(linje) - len(linje.lstrip("\t"))
        else:
            niva = (len(linje) - len(linje.lstrip(" "))) // 2
        tekst = linje.strip()
        if tekst.startswith("•"):
            tekst = tekst[1:].strip()
        elif niva == 0:
            continue  # rotnoden, dokumenttittelen
        lenke = None
        m = re.match(r"^(.*) \((https?://[^)]+)\)$", tekst)
        if m:
            tekst, lenke = m.group(1), m.group(2)
        noder.append((niva, tekst, lenke))
    return noder


def er_intern(url):
    return any((url or "").startswith(b) for b in BASER)


def sti_av_url(url):
    for b in BASER:
        if url.startswith(b):
            d = url[len(b):].strip("/")
            break
    else:
        return None
    if not d:
        return None
    deler = d.split("/")
    if len(deler) == 1:
        return os.path.join("content", deler[0], "_index.md")
    return os.path.join("content", deler[0], deler[1] + ".md")


def front_matter_tittel(sti):
    try:
        t = open(sti, encoding="utf-8").read()
    except OSError:
        return None
    m = re.search(r'^\s*title\s*=\s*"(.*)"\s*$', t, re.M)
    return m.group(1) if m else None


def sett_felt(tekst, felt, verdi):
    linjer = tekst.split("\n")
    slutt = linjer.index("+++", 1)
    ny = "%s = %s" % (felt, verdi)
    for i in range(1, slutt):
        if re.match(r"^\s*%s\s*=" % felt, linjer[i]):
            linjer[i] = ny
            return "\n".join(linjer)
        if linjer[i].lstrip().startswith("[["):
            linjer.insert(i, ny)
            return "\n".join(linjer)
    linjer.insert(slutt, ny)
    return "\n".join(linjer)


def rydd_duplikater(utfor):
    """iCloud lager av og til «fil 2.md». Fjern dem når de er identiske."""
    import filecmp
    fjernet = []
    for rot, _, filer in os.walk(C):
        for f in filer:
            m = re.match(r"^(.*) \d+(\.md)$", f)
            if not m:
                continue
            dup = os.path.join(rot, f)
            orig = os.path.join(rot, m.group(1) + m.group(2))
            if os.path.exists(orig) and filecmp.cmp(dup, orig, shallow=False):
                fjernet.append(os.path.relpath(dup, ROT))
                if utfor:
                    os.remove(dup)
    return fjernet


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    kartfil = sys.argv[1]
    utfor = "--apply" in sys.argv
    noder = les_kart(kartfil)
    unntak = les_unntak()

    seksjoner = []       # (tittel, sti, vekt)
    sider = []           # (seksjonsindeks, tittel, sti|None, lenke|None)
    gjeldende = None
    for niva, tittel, lenke in noder:
        if niva == 1:
            gjeldende = len(seksjoner)
            seksjoner.append([tittel, sti_av_url(lenke) if lenke else None, lenke])
            continue
        if gjeldende is None:
            continue
        er_side = (niva == 2 or er_intern(lenke)) and tittel not in unntak
        if not er_side:
            continue
        sider.append([gjeldende, tittel, sti_av_url(lenke) if er_intern(lenke) else None, lenke])

    nye, flyttet, vekt, titler, foreldrelose, mindnode = [], [], [], [], [], []

    # seksjoner
    for i, (tittel, sti, lenke) in enumerate(seksjoner, start=1):
        if sti is None:
            slug = slugify(tittel)
            sti = os.path.join("content", slug, "_index.md")
            nye.append(sti)
            mindnode.append({"handling": "sett_lenke", "node": tittel,
                             "lenke": "%s/%s/" % (SKRIV_BASE, slug)})
            if utfor:
                os.makedirs(os.path.join(ROT, "content", slug), exist_ok=True)
                open(os.path.join(ROT, sti), "w", encoding="utf-8").write(
                    '+++\ntitle = "%s"\nweight = %d\n+++\n' % (tittel, i))
            seksjoner[i - 1][1] = sti
            continue
        full = os.path.join(ROT, sti)
        if not os.path.exists(full):
            nye.append(sti)
            if utfor:
                os.makedirs(os.path.dirname(full), exist_ok=True)
                open(full, "w", encoding="utf-8").write(
                    '+++\ntitle = "%s"\nweight = %d\n+++\n' % (tittel, i))
            continue
        t = open(full, encoding="utf-8").read()
        fm = front_matter_tittel(full)
        if fm and fm != tittel:
            titler.append((sti, fm, tittel))
        ny = sett_felt(t, "weight", i)
        if ny != t:
            vekt.append(sti)
            if utfor:
                open(full, "w", encoding="utf-8").write(ny)

    # sider
    teller = {}
    for seksjonsindeks, tittel, sti, lenke in sider:
        seksjonssti = seksjoner[seksjonsindeks][1] or ""
        seksjonsslug = seksjonssti.split(os.sep)[1] if seksjonssti else slugify(seksjoner[seksjonsindeks][0])
        teller[seksjonsslug] = teller.get(seksjonsslug, 0) + 1
        v = teller[seksjonsslug]
        if sti is None:
            slug = slugify(tittel)
            sti = os.path.join("content", seksjonsslug, slug + ".md")
            nye.append(sti)
            mindnode.append({"handling": "sett_lenke", "node": tittel,
                             "lenke": "%s/%s/%s/" % (SKRIV_BASE, seksjonsslug, slug)})
            if utfor and not os.path.exists(os.path.join(ROT, sti)):
                os.makedirs(os.path.join(ROT, "content", seksjonsslug), exist_ok=True)
                open(os.path.join(ROT, sti), "w", encoding="utf-8").write(
                    '+++\ntitle = "%s"\nweight = %d\n+++\n' % (tittel, v))
            continue
        full = os.path.join(ROT, sti)
        naa_seksjon = sti.split(os.sep)[1]
        if naa_seksjon != seksjonsslug:
            nysti = os.path.join("content", seksjonsslug, os.path.basename(sti))
            flyttet.append((sti, nysti))
            mindnode.append({"handling": "sett_lenke", "node": tittel,
                             "lenke": "%s/%s/%s/" % (SKRIV_BASE, seksjonsslug,
                                                     os.path.basename(sti)[:-3])})
            fantes = os.path.exists(full)
            if utfor and fantes:
                os.makedirs(os.path.join(ROT, "content", seksjonsslug), exist_ok=True)
                os.rename(full, os.path.join(ROT, nysti))
            if not utfor:
                # tørrkjøring: fila ligger fortsatt på gammel plass
                if fantes:
                    continue
            sti, full = nysti, os.path.join(ROT, nysti)
        if not os.path.exists(full):
            nye.append(sti)
            if utfor:
                open(full, "w", encoding="utf-8").write(
                    '+++\ntitle = "%s"\nweight = %d\n+++\n' % (tittel, v))
            continue
        t = open(full, encoding="utf-8").read()
        fm = front_matter_tittel(full)
        if fm and fm != tittel:
            titler.append((sti, fm, tittel))
        ny = sett_felt(t, "weight", v)
        if ny != t:
            vekt.append(sti)
            if utfor:
                open(full, "w", encoding="utf-8").write(ny)

    # sider uten node
    kjente = {s[2] for s in sider if s[2]} | {s[1] for s in seksjoner if s[1]}
    for rot, _, filer in os.walk(C):
        for f in sorted(filer):
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(rot, f), ROT)
            if os.path.dirname(rel) == "content":
                continue  # om, personvern, kontakt ...
            if rel not in kjente:
                foreldrelose.append(rel)
                mindnode.append({"handling": "opprett_node",
                                 "tittel": front_matter_tittel(os.path.join(rot, f)) or f,
                                 "seksjon": rel.split(os.sep)[1],
                                 "lenke": SKRIV_BASE + "/" + rel[len("content/"):].replace("/_index.md", "/").replace(".md", "/")})

    duplikater = rydd_duplikater(utfor)

    print("== %s ==" % ("UTFØRT" if utfor else "RAPPORT, ingenting endret"))
    for navn, liste in (("Nye sider", nye), ("Flyttet", flyttet),
                        ("Ny weight", vekt), ("Sider uten node", foreldrelose),
                        ("Duplikater fjernet", duplikater)):
        print("%s: %d" % (navn, len(liste)))
        for x in liste:
            print("   ", x)
    print("Titler som er ulike (endres ikke): %d" % len(titler))
    for sti, fm, node in titler:
        print("    %s\n        side: %s\n        kart: %s" % (sti, fm, node))
    print("\n--- MINDNODE-HANDLINGER (JSON) ---")
    print(json.dumps(mindnode, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
