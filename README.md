# ryddedagen.no

## Forutsetninger

Installer [Hugo](https://gohugo.io/getting-started/installing/).

## Jobb med forhåndsvisning

For å vise en forhåndsvisning må du være i prosjektmappen og kjøre `hugo serve`.

```shell
cd ryddedagen.no
hugo serve
```

## Bygg nettsiden

For å bygge nettsiden må du være i prosjektmappen og kjøre `hugo`.

```shell
cd ryddedagen.no
hugo
```

Denne kommandoen genererer alle filene som hører til nettsiden i en mappe ved
navn `public`. Innholdet i `public` kan nå kopieres til webhotellet.

## Shortcoden `handling`

Konkrete handlinger skrives med shortcoden `handling`, som gir en avkryssings-
boks i et Bootstrap-kort:

```text
{{< handling
    id="skatteetaten-kontaktinfo"
    tittel="Sjekk kontaktinformasjonen din"
    sti="Konto for utbetalinger fra Skatteetaten"
>}}
Kontroller at mobilnummer og e-postadresse stemmer.
{{< /handling >}}
```

| Parameter | Påkrevd | Forklaring |
| --- | --- | --- |
| `id` | Ja | Unik nøkkel. Bruk sideprefiks, f.eks. `skatteetaten-innboks`. |
| `tittel` | Nei | Kort handlingstekst. Uten tittel blir innholdet klikkflaten. |
| `sti` | Nei | Hvor man klikker videre på undersiden. Vises som brødsmulesti. |
| `stilenke` | Nei | Adresse siste ledd i stien lenkes til. Krever `sti`. |
| `bilde` | Nei | Overstyrer filnavnet. Trengs normalt ikke, se under. |
| `bildetekst` | Nei | Vises under bildet og brukes som alt-tekst. |
| `ikon` | Nei | Font Awesome-klasser. Uten denne vises ingen ikon. |

Avkryssingen lagres i `localStorage` av skriptet nederst i
`layouts/_default/baseof.html`, under nøkkelen `ryddedagen:handling:<id>`.
Det betyr at den følger nettleseren, ikke brukeren: bytter du enhet eller
tømmer nettleserdata, er avkryssingene borte. Ingenting sendes til serveren.

Fordi nøkkelen er global, må `id` være unik på tvers av hele nettstedet.
Bruker du samme `id` to ganger på én side, varsler skriptet i nettleser-
konsollen.

`id` er permanent. Endrer du den etter publisering, mister alle som har
krysset av akkurat den avkryssingen.

### Stien

Overskriftene på en side følger tjenestens egne undersider, så `sti` skal
ikke gjenta dem. Den sier hvor man klikker videre *inne på* undersiden, og
står tom når handlingen ligger rett på den. Flere trinn skilles med `>`
eller `→`:

```text
sti="Skjemaer > Konto for utbetalinger → Endre konto"
```

`stilenke` lenker siste ledd i stien dit man faktisk skal:

```text
sti="Min side > Om meg"
stilenke="https://www.skatteetaten.no/person/..."
```

Bare siste ledd blir lenke — det er destinasjonen; leddene foran er veien
dit. Lenken åpnes i ny fane, slik at sjekklista blir stående med
avkryssingene synlige. Den får en `aria-label` som gjentar teksten og legger
til at den åpnes i ny fane, både fordi flere kort kan ha et ledd som heter
det samme, og fordi en lenke som bytter fane bør si fra.

Det blir en brødsmulesti med piler mellom trinnene. Pilen settes med
`--bs-breadcrumb-divider` i `static/style.css`. Bootstrap setter aldri den
variabelen selv, bare leser den med `/` som reserveverdi, så den overstyringen
virker også når `style.css` lastes før Bootstrap. Den er en `<ol>`
uten `<nav>` rundt, med vilje: dette er ikke navigasjon på siden, bare en
beskrivelse av hvor man klikker, og et navigasjonslandemerke uten lenker
ville bare forvirret skjermlesere.

### Skjermbilder

Legg skjermbildet i `static/bilder/` med `id`-en som filnavn, altså
`static/bilder/skatteetaten-kontaktinfo.png`. Da finner shortcoden det
selv, og «Vis skjermbilde» dukker opp på kortet ved neste bygg uten at
innholdsfila trenger å vite om det. `png`, `jpg`, `jpeg`, `webp`, `avif`
og `gif` prøves i den rekkefølgen, og første treff vinner. Bildet lastes
først når noen åpner det, og hele mekanismen er ren HTML — `<details>`,
ingen JavaScript.

Klikker man på bildet, forstørres det i et `<dialog>` med mørk bakgrunn.
Esc, fokushåndtering og bakgrunn tar nettleseren seg av; klikk utenfor
bildet eller på krysset lukker også. Dialogen lages av skriptet i
`baseof.html` første gang noen klikker, så den finnes ikke i kildekoden.
Uten JavaScript er bildet en helt vanlig lenke til bildefila, så den
åpnes direkte i stedet. Cmd-, Ctrl- og Shift-klikk slipper også gjennom
til nettleseren, så «åpne i ny fane» virker som folk forventer.

Krysser man av handlingen, faller skjermbildet sammen igjen. Det skjer
bare når noen faktisk huker av, ikke ved innlasting, så et bilde man har
åpnet selv blir stående åpent — også på et kort som allerede er avkrysset.

Alt-teksten kan ikke utledes av et filnavn. Uten `bildetekst` blir den
`Skjermbilde: <tittel>`, som er dekkende nok til at HTML5-valideringen
går gjennom og skjermlesere får noe fornuftig. Skriver du `bildetekst`,
brukes den både som alt-tekst og som tekst under bildet.

Legger du inn et bilde mens `hugo serve` kjører, kan det hende du må
starte serveren på nytt — nye filer i `static/` utløser ikke alltid at
shortcoden kjøres om igjen.

## Fremdriftsvisning

Fremdriften vises to steder, og begge fylles av skriptet nederst i
`layouts/_default/baseof.html`:

- **Tallet** ligger i `layouts/partials/fremdrift.html` og rendres inn i
  navbarens andre rad, til høyre for hvilken side man står på. Det gjelder
  alltid gjeldende side, og er skjult på sider uten handlinger.
- **Stolpen** ligger i `layouts/partials/sidelinje.html`, absolutt
  posisjonert mot navbaren, så den legger seg i underkanten av hele baren
  uansett hvor mange rader den har. Tre piksler høy, koster ingen høyde.
- **Nullstillingsknappen** ligger nederst på siden
  (`layouts/partials/nullstill.html`, rendret fra `single.html`). Den hørte
  opprinnelig sammen med tallet, men i navbaren ble det for trangt på
  telefon: baren brøt over to linjer, og da sklir innholdet inn under den
  faste baren. Nederst er den dessuten der man er når man vil begynne på
  nytt. Den vises først når noe faktisk er krysset av.

Begge starter skjult og vises først når JavaScript har talt opp, så de
viser aldri feil tall for noen uten JavaScript. Når alt er gjort, blir
begge grønne — samme grønn som et avkrysset kort. Fargen er aldri eneste
signal: teksten sier «Alle 13 er gjort».

## Hvor man er i menyen

`nav.html` setter `active` på seksjonsknappen når gjeldende side ligger
under den (`.IsAncestor`), i tillegg til `active` på selve siden inne i
nedtrekket. Bootstrap skiller den aktive seksjonen bare med en mørkere
tekstfarge, som er lett å overse i en rad med fjorten punkter, så
`static/style.css` gjør den tydeligere: primærfarge gjennom Bootstraps
egen `--bs-navbar-active-color`, halvfet tekst, og en strek — understrek
når menyen er en rad, loddrett strek til venstre når den er en liste.
Streken er lagt med `inset box-shadow` og ikke `border`, så den ikke
flytter noe.

Knappen får også `aria-current="true"`, så seksjonen er markert for
skjermlesere og ikke bare visuelt. Sida inne i nedtrekket har fortsatt
`aria-current="page"`.

## Navbarens andre rad

`layouts/partials/sidelinje.html` er raden under menyen: hvilken side man
står på til venstre, fremdriften til høyre. Den er en del av den faste
baren, så den blir stående når man skroller og tittelen i inngangskortet
har rullet ut av syne. Seksjonen står foran sidetittelen med samme pil som
stiene i handlingskortene. Raden sløyfes på forsiden og på sider uten
tittel.

Baren ligger i vanlig flyt, med `sticky-top` på `<header>` og ikke på
`<nav>`: et sticky element kleber bare så lenge forelderen er i bildet, og
`<header>` er ikke høyere enn baren selv. Da kleber den seg til toppen når
man skroller, og skyver innholdet ned av seg selv når hamburgermenyen slås
ut, i stedet for å legge seg over det. Det er også grunnen til at `body`
ikke har noen utregnet toppavstand og at det ikke finnes noe måleskript —
begge deler hørte til en tidligere `fixed-top`-variant.

To ting i `static/style.css` holder dette oppe:

- Navbaren er lagt om til `flex-direction: column`, som stabler de to
  radene på alle bredder. Uten det klemmes den andre raden inn på
  menyraden fra `xl` og opp, der Bootstrap setter `flex-wrap: nowrap`.
  Selektoren er `nav.navbar` fordi `style.css` lastes før Bootstrap og
  trenger et element pluss en klasse for å vinne.

  **Ikke sett `flex-wrap` i den regelen.** Bootstrap gir `.container-fluid`
  inne i navbaren `flex-wrap: inherit`, så `nowrap` der slår også ut
  menyens evne til å brekke ned på egen linje når hamburgeren åpnes — da
  legger den seg som en høy kolonne ved siden av merkenavnet i stedet.
  Kolonneretningen stabler radene helt uten at wrap røres.

- Samme regel setter `position: relative`. Fremdriftsstolpen er absolutt
  posisjonert mot baren, og uten `fixed-top` er ikke baren lenger
  posisjonert av seg selv — da ville stolpen lagt seg mot sida i stedet.

Menyen har fjorten punkter og renner ut av baren fra `xl` og opp. Det er en
egen sak, og var det også før den andre raden kom til.

To fallgruver hvis du endrer markupen: `style.css` lastes før Bootstrap,
så egne regler trenger to klasser for å vinne, og Bootstrap-utilities som
`.text-body-secondary` og `.d-flex` er `!important` og slår både egne
farger og `hidden`-attributtet.

## Shortcoden `inngang`

Sidens inngangskort: skjermbilde av tjenesten, en kort innledning,
hvordan man logger inn, og knappen inn. Ett per side, øverst.

```text
{{< inngang
    url="https://www.skatteetaten.no/person/"
    knapp="Logg inn på skatteetaten.no"
    innlogging="ID-porten"
>}}
Hos Skatteetaten kan du sjekke skattekort og skattegjeld, men det er også
etaten som har tatt over Folkeregisteret.
{{< /inngang >}}
```

| Parameter | Påkrevd | Forklaring |
| --- | --- | --- |
| `url` | Ja | Adressen knappen går til. Åpnes i ny fane. |
| `knapp` | Nei | Knappetekst. Standard `Gå til tjenesten`. |
| `stil` | Nei | Bootstrap-variant uten `btn-`. Standard `outline-primary`. |
| `innlogging` | Nei | Hvordan man logger inn, f.eks. `ID-porten`. |
| `navn` | Nei | Tjenestens navn. Sløyf den når innledningen sier det. |
| `bilde` | Nei | Overstyrer filnavnet. Trengs normalt ikke, se under. |
| `bildetekst` | Nei | Beskriver bildet, og brukes som alt-tekst. |

Kortet rendrer sidens `<h1>`, så `layouts/_default/baseof.html` hopper over
tittelen på sider som bruker shortcoden. Derfor hører kortet øverst på
siden — står det lenger nede, havner overskriften midt i teksten.

Oversiktsbildet finnes på samme måte som skjermbildene i handlingene, men
med sidens eget filnavn: `static/bilder/skatteetaten-mine-sider.png` for
`content/det-offentlige/skatteetaten-mine-sider.md`. Uten bilde blir kortet
bare tekst og knapp i full bredde, så det haster ikke å legge det inn.

Teksten står til venstre og bildet til høyre, så øyet møter hva siden
handler om før illustrasjonen. På smale skjermer stables de, med teksten
øverst.

Knappen er `outline-primary` og ikke fylt. Blått er ellers bare en tynn
aksent på siden — venstrekanten på kortene, fremdriftsstolpen, lenkene — og
en fylt blå flate var det eneste som brøt med det. `stil` bytter den om du
vil ha den tyngre.

Kortet har med vilje ingen farget venstrekant. Den tilhører handlingene, og
inngangen er ikke en handling. `navn` er et avsnitt og ikke en overskrift,
av samme grunn som i `notis`.

Om logoer: nettstedet er en uavhengig veiviser, ikke en offentlig portal.
Skjermbildet viser hva tjenesten er uten å låne noen andres merke, og uten
å antyde at de står bak siden. Det er grunnen til at kortet viser et
skjermbilde og ikke en logo.

## Shortcoden `knapp`

For en enkeltstående knapp i brødteksten. Sidens hovedknapp hører hjemme i
`inngang` i stedet.

```text
{{< knapp url="https://www.skatteetaten.no/person/" >}}
Logg inn på skatteetaten.no
{{< /knapp >}}
```

`stil` velger Bootstrap-variant uten `btn-`-prefikset (standard `primary`),
og `egenfane="nei"` åpner lenken i samme fane.

Den gamle `[[knapper]]`-blokken i front matter virker fortsatt, og de
øvrige sidene bruker den. `layouts/_default/single.html` rendrer begge
deler, så migreringen kan tas én side om gangen.

## Shortcoden `notis`

En liten merknad i brødteksten — et sidespor, en avklaring, en
henvisning videre:

```text
{{< notis tittel="Leter du etter fullmakt og tilgangsstyring?" >}}
Dette håndteres av innstillinger på Altinn, ikke på Skatteetaten.
{{< /notis >}}
```

`tittel` blir et avsnitt i halvfet, ikke en overskrift. Det er med vilje:
en merknad skal ikke inn i overskriftshierarkiet på linje med bolkene av
handlinger, hvor den ville sett ut som enda en bolk i innholdsoversikten.

`stil` velger Bootstrap-variant uten `alert-`-prefikset. Standard er
`secondary`, som er dempet nok til at den ikke roper, og som ikke har den
blå venstrekanten handlingskortene har. Bruk `warning` eller `danger` bare
når noe faktisk kan gå galt — ellers slutter folk å se forskjell.

Notisen har bevisst ingen `role="alert"`, selv om Bootstrap-dokumentasjonen
viser det. Den rollen er et live-område for meldinger som dukker opp mens
man bruker siden, og ville fått skjermlesere til å avbryte opplesningen for
noe som har stått der hele tiden.

## Markdownlint-regelen MD034

Fordi URL-en nå står i brødteksten og ikke i front matter, ser
markdownlint den som en bar URL. Derfor er regelen `no-bare-urls`
(MD034) slått av i `.markdownlint.json`. Vil du heller beholde regelen,
kan du ta den på igjen og sette
`<!-- markdownlint-disable-next-line MD034 -->` over hver knapp.

## Markdownlint

Vi bruker markdownlint-verktøyet i dette prosjektet. Enhver merge må gjennom en
markdownlint-kontroll. For å unngå for mange markdownlint-commits, bruker vi
[https://dlaa.me/markdownlint/](https://dlaa.me/markdownlint/) til å kontrollere
dokumentene før vi commiter.

## HTML5-validering

Hver merge går gjennom en HTML5-validering. `hugo`-jobben i
`.github/workflows/main.yml` bygger nettsiden med `hugo --minify` og kjører
[v.Nu](https://validator.github.io/validator/) mot alt som havner i `public/`.
Valideringen kjøres to ganger: først med `--show-warnings`, som bare er til
informasjon, og så uten, og det er den siste som feller bygget hvis den finner
feil.

For å slippe unødvendige rettecommits kan du kontrollere en side før du
commiter, enten på [html5.validator.nu](https://html5.validator.nu) eller
lokalt:

```shell
pip install html5validator
hugo --minify
html5validator --root public/ --show-warnings
```
