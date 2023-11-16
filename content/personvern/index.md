+++
title = "Personvern på pdog.no"
aliases = [
    "personsvern",
    "privacy"
]
[menu]
main = { weight = 9, parent = "Personvern og sikkerhet" }
+++

<!-- markdownlint-disable MD042 -->

{{% ingress %}}

Personvern er en grunnleggende rettighet, også når du besøker nettsider. Jeg ønsker ikke å samle
inn informasjon om deg utover det som er strengt nødvendig for at du skal kunne bruke nettsiden.
I denne artikkelen har jeg dokumentert alle de tilfeller jeg vet at denne nettsiden samler inn
informasjon om deg, og jeg prøver å oppdatere den fortløpende når jeg får ny informasjon,
eller når jeg involverer flere prosjekter.

{{% /ingress %}}

##### Eksterne lenker

Så langt det lar seg gjøre, prøver jeg å markere alle eksterne lenker på pdog.no. Jeg gjør dette
på tre forskjellige måter:

- [farve lenken blå og understreke den når musepekeren beveger seg over lenken](#)
- oppgi rotadressen i parentes, eksempel: [Les mer (pdog.no)](#)
- bruke {{< ext >}}-symbolet, eksempel: [Les mer (pdog.no) {{< ext >}}](#)

Noen sider er fulle av lenker. Da vil det være synlig høyt i artikkelen at siden inneholder
mange eksterne lenker.

##### Kontakt på forskjellige kanaler

Rundt om kring på nettsiden oppgis det min kontaktinformasjon. Hvis du kontakter meg, vil
informasjonen du sender fra deg, som for eksempel det oppgitte navnet, e-postadressen, telefonnummer
og så videre, bli tilgjengelig for meg og lagres på mine enheter og i internettlagringstjenester
jeg abonnerer på.

##### Eksterne ressurser

- Nettsiden er bygget på et rammeverk som henter eksterne ressurser: [Bootstrap (getbootstrap.com)
{{< ext >}}][bootstrap].
- Jeg henter også inn eksterne ikoner fra [Font Awesome (fontawesome.com)
{{< ext >}}][fontawesome].

##### Netthotellets statistikkfunksjon

Jeg har valgt å holde pdog.no på et netthotell hos det norske selskapet DOMENESHOP AS. Tjenerne
ligger i Norge. Som en del av tjenesteleveransen tilbyr selskapet en egen [statistikkside jeg
kan logge inn på (domeneshop.no) {{< ext >}}][domeneshop-stat]. Dette kjører på
[AWStats-programvaren (awstats.org) {{< ext >}}][awstats].

Jeg kan logge inn på tjenesten
ved hjelp av innloggingsdetaljene til FTP-tjeneren min, og se informasjon om for eksempel:

- antall unike besøkende og klikk fordelt på tid
- noenlunde maskerte datamaskinadresser, samt hvilke land disse stammer fra
- operativsystemer og nettlesere
- opprinnelig kilde for besøket

Selv om jeg har tilgang på dette, betyr det ikke at jeg er interessert i informasjonen jeg får
presentert, og bruker den ikke i utviklingen av siden. Jeg kan så vidt jeg vet ikke skru dette
av.

##### Innebygde elementer fra Google Maps og YouTube

Noen av sidene på pdog.no bruker innebygde elementer fra Google Maps, som kan være underlagt
[Googles personvernserklæring (safety.google){{< ext >}}][google].

Noen av sidene på pdog.no bruker innebygde elementer fra YouTube, som kan være underlagt
[YouTube API Services Terms of Service (developers.google.com) {{< ext >}}][yt].

##### Innebygde elementer fra Ruter

Noen av sidene på pdog.no bruker innebygde elementer fra RUTER AS, som har sine egne regler for
[Personvern i Ruters tjenester (ruter.no) {{< ext >}}][ruter].

Ved henvendelse til Ruters personvernombud i januar 2021 ble det bekreftet at innebygde elementer
ikke installerer noen sporere på brukerens enhet.

Ruters sanntidsskjerm (MON) har en egen personvernsside på
[MON og personvern (ruter.no) {{< ext >}}][mon].

##### Hvordan finansieres pdog.no uten å samle inn brukerdata og selge annonser?

Jeg tjener ikke en krone på pdog.no, og alt jeg har brukt på siden er egne oppsparte midler. Jeg
selger ikke data eller annonser. Hvis du vil, kan du støtte prosjektet økonomisk:
[Gi et økonomisk bidrag](../finansiering).

##### Kontaktinformasjon

Hvis du har spørsmål om personvernhåndteringen på pdog.no eller tilstøtende prosjekter,
ta gjerne kontakt med meg på [personvern@pdog.no](mailto:personvern@pdog.no).

Du må gjerne stjele hele eller deler av denne personvernerklæringen for å bruke i dine egne
prosjekter.

[bootstrap]: https://getbootstrap.com/docs/4.6/getting-started/introduction/
[google]: https://safety.google/privacy/
[fontawesome]: https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use
[yt]: https://developers.google.com/youtube/terms/api-services-terms-of-service-emea#user-privacy
[mon]: https://ruter.no/fa-hjelp/vilkar/personvern/mon-og-personvern  
[domeneshop-stat]: https://domene.shop/faq?section=25&id=82
[awstats]: http://www.awstats.org
[ruter]: https://ruter.no/fa-hjelp/vilkar/personvern/
