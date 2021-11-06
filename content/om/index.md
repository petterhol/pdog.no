+++
title = "Om pdog.no"
lastmod = 2020-10-06T22:00:00
aliases = [
    "sidekart",
    "personvern",
    "lisens",
]
[menu]
main = { weight = 1, parent = "Petter" }
+++

{{% ingress %}}

Dette er personlig nettside for Petter Holstad. Her kan du lese mer om nettsidens formål, sidekart,
personvernserklæring, versjonshistorikk, teknologi, bidragsytere, lisens og innspill.

{{% /ingress %}}

{{< accordion >}}

{{% card header="Formål og innholdsoversikt" %}}

Før du leser videre: denne nettsiden er _i all hovedsak_ et hobbyprosjekt hvor jeg lærer meg
selv å lage nettsider, koding og det å jobbe med GitHub. Bare gleden av å lage nettsiden er mer
enn nok for meg.

Når nettsiden først finnes, er det greit å vite at den oppyller disse formålene:

- Landingsside for domenet jeg eier, som jeg også bruker som e-postdomene.  
- Oversikt over [komplett kontaktinformasjon](../kontaktinfo).  
- [Veibeskrivelse til min bolig](../visit).  
- Et sted å ha en offentlig [CV](../cv).  
- Landingsside for mitt enkeltpersonsforetak [Helt og Holdent](../heltogholdent).  
- Noen artikler om [teknologi](../teknologi).  
- Noen artikler om [kart og reising](../kartogreiser).  
- Et sted legge ut [luftfoto](../luftfoto).  
- En minneside over [Orddelingsmafiaen](../orddelingsmafiaen).
- Et sted å starte nye prosjekter som kan bli egne nettsider etterhvert.  
- En rekke andre landingssider og formål som ikke er offentlig tilgjengelig.

Nettsiden utgjør i aller høyeste grad et hobbyprosjekt, med ingen eller liten verdi for andre. Jeg
lærer mye ved å drive med nettsideutvikling. Noen av ideene mine, inkludert artiklene mine, bruker
jeg som selvstendige sider for å lenke når jeg er i en diskusjon med noen om det temaet jeg har
skrevet om.

{{% /card %}}

{{% card header="Oversikt over domener" %}}

- pdog.no (tilknyttet webhotell og e-post)  
- p-dog.no (alternativ staving av hoveddomenet)  
- petterholstad.no (annet domene brukt til epost)  
- heltogholdent.no  (lenkes direkte til [siden om enkeltpersonsforetaket](../heltogholdent))

Alle domenene er registert hos [Domeneshop {{< ext >}}](https://domene.shop), mens
e-posttjeneren er iCloud.

{{% /card %}}

{{% card header="Personvernserklæring" %}}

**Hovedregel:** Jeg vil ikke spore din aktivitet på nettsiden. Gjennom min leverandør av
internetthotell får jeg noe bruksstatistikk på siden, men jeg bruker det ikke. Det er ikke
installert noe tredjepartsprogramvare som kan spore deg fra min side. Jeg har ingen steder
man kan logge inn.

**Untak**: Se denne oversikten over unntak fra hovedregelen:

- Innhenting av eksterne ressurser: For at nettsiden skal fungere må den hente inn eksterne
ressurser fra [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/). Jeg
henter også inn eksterne ikoner fra
[Font Awesome](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use).

- Kontaktskjema: Jeg bruker et kontaktskjema flere steder på nettsiden. Dette skjemaet bruker et
script fra [Domeneshop {{< ext >}}](https://domene.shop/faq?id=61&section=21), og sender
e-poster til meg direkte. Innholdet, samt personopplysningene du har valgt å legge ved, blir bare
brukt til det formålet som var klart da du sendte inn skjemaet. Opplysningene i skjemaet lagres
ingen andre steder enn i min personlige e-postkasse.

- Eksterne lenker: Nettsiden lenker til flere eksterne nettsider. Alle eksterne nettsider er
markert med {{< ext >}}-ikonet.

- Innebygde elementer på nettsiden: Nettsidene [Personlig flykart](reisekart),
[Silicon Valley og omegn](sv), [The Tim
Traveller](timtraveller) og [Tom Scott](tomscott) bruker alle innbygde elementer fra
Google MyMaps.
Nettsiden [Kart og kompass](visitt/kartogkompass) bruker innebygde elementer fra Google Maps.
Alt er underlagt
[Googles personvernserklæring {{< ext >}}](https://safety.google/privacy/). Ruters reiseforslag kan
være underlagt
[Personvern i Ruters tjenester {{< ext >}}](https://ruter.no/fa-hjelp/vilkar/personvern/).
Innebygde elementer fra Ruter bruker i følge Ruters personvernsombud januar 2021 ingen
sporere.
Ruters sanntidsskjerm (MON) har en egen personvernsside på
[MON og personvern {{< ext >}}][mon] Hvis du havner inn på [rickroll.htm](http://pdog.no/rickroll)
har du sannsynligvis blitt
utsatt for et [Grabify {{< ext >}}](https://grabify.link)-forsøk.  Dette henter
informasjon din klient sender fra deg, som IP-adresse, nettleser med mer. Du kan lese mer
om denne på siden min om [scambaiting](../scambaiting).

- Sider med YouTube-spiller kan være underlagt
[YouTube API Services Terms of Service {{< ext>}}][yt].

- Innsendinger av bidrag i min [gjestetilfredsstillelsesundersøkelse](pdog.no/survey) er underlagt
egne personvernsregler for innsendinger.

Jeg jobber stadig for å forbedre denne oversikten med mer konkret informasjon.

[yt]: https://developers.google.com/youtube/terms/api-services-terms-of-service-emea#user-privacy
[mon]: https://ruter.no/fa-hjelp/vilkar/personvern/mon-og-personvern  

{{% /card %}}

{{% card header="Versjonshistorikk, bidragsytere og teknologi" %}}

**v1:** Siden brukte ren HTML- og CSS-koding. Mye av kodingen ble gjort av Stig Johan Berggren, mens
det redaksjonelle innholdet ble i hovedsak utformet av Petter Holstad, med diverse innspill.

**v2:** Den nåværende versjonen av nettsiden er bygget på et
[Bootstrap-rammenettverk. {{< ext >}}](https://getbootstrap.com) Innholdet skrives i
[Markdown-språket {{< ext >}}](https://daringfireball.net/projects/markdown/syntax), og
konverteres med
[Hugo {{< ext >}}](https://gohugo.io). På min Mac bruker jeg appene
[BBEdit {{< ext>}}](https://www.barebones.com/products/bbedit/) til å redigere
.md- og .html-filene, [Pixelmator {{< ext >}}](https://www.pixelmator.com) til
bildemanipulering og
[FileZilla {{< ext >}}](https://filezilla-project.org) til FTP-overføringer. På GitHub sjekkes
filene etter markdownlint og hugo før de flettes i main. Nettsiden er utviklet av Stig Johan
Berggren, innholdet er i hovedsak av Petter Holstad med diverse bidragsytere.

**v2.1**: Denne versjonen skal implementere oversettelser - i første omgang engelsk. Foreløpig er
dette bare på idéstadiet, og kan følges på [GitHubs prosjektsider {{< ext >}}](git2).

[git2]: https://github.com/Stigjb/pdog.no/projects/1

{{% /card %}}

{{% card header="Lisens" %}}

I all hovedsak ønsker jeg å tilby det jeg lager relativt fritt tilgjengelig for ikke-kommersielle
formål. Jeg har derfor valgt å bruke
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International CC-BY-NC-SA 4.0 {{< ext >}}][cc]
til det aller meste av innholdet på nettsiden. Med mindre annet er nevnt, gjelder den følgende:

- Nettsidens tekst.
- Bilder på nettsiden.
- Kildekoden til nettsiden, med unntak av innebygde tredjepartselementer.

Noen bilder på nettsiden er opphavsrettbeskyttet eller beskyttet av en annen lisens. Dette gjelder
alle innebygde elementer (Google MyMaps, YouTube m.m).

I de fleste tilfeller er andre lisenser markert med følgende:

{{< lisens
  type="Eksempelinnhold"
  lisensnavn="Eksempel"
  lisenslink="#"
  >}}
  
Alt som ikke faller innunder definisjonen over, vil falle under ordinær opphavsrett.

Hvis du vil bruke noe kommersielt, eller er i tvil på hvordan du kan bruke innholdet,
er det ikke verre enn at du bare [tar kontakt](../kontaktinfo) med meg.

[cc]: https://creativecommons.org/licenses/by-nc-sa/4.0/

{{% /card %}}

{{% card header="Språk" %}}

Jeg prøver å opprettholde et godt språk på siden. Foreløpig er tekstene skrevet på norsk
(bokmål), men jeg prøver å oversette til engelsk etterhvert.

Noen språkregler jeg selv prøver å følge:

- Nettsidens domene skal uttales uten punktum og skråstrek. Eksempel: "pdog.no" -->
"pe dågg no". Eksempel: "pdog.no/kylling" --> "pe dågg no kylling".
- Hvis det er finnes et norsk ord for noe man kanskje normalt bruker et
engelsk begrep for, skal man i hovedsak bruke det norske uttrykket. En forutsetning
er at det må være oppført i en ordbok, brukt av norsk media eller på annen måte etablert.

{{% /card %}}

{{% card header="Korrigering, korrektur, bidrag, betatesting og tilbakemeldinger" %}}

Jeg tar hjertelig imot alle bidrag og tilbakemeldinger til nettsiden. Hvis du er kjent med GitHub og
Markdown, er kodeforbedringer og innholdsbidrag hjertelig velkommen der:
[petterhol/pdog.no {{< ext >}}][git].

Følgende prosjekter har spesifikke instruksjoner for hvordan du best gir tilbakemelding:

- Tom Scott (nedlastbar, lesbar HTML-fil)

Forøvrig er alle andre tilbakemeldinger best å [kontakte meg](../kontaktinfo) for.

Hvis du vil være betatester, korrekturleser eller ha en annen funksjon, er du hjertelig velkommen
til det også.

[git]: https://github.com/petterhol/pdog.no

{{% /card %}}

{{< /accordion >}}
