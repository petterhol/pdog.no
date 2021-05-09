+++
title = "E-posthåndtering med 'catch all'"
linkTitle = "E-post: Catch-all"
lastmod = 2020-10-06T22:00:00
[menu]
main = { weight = 5, parent = "Teknologi" }
+++

<!-- markdownlint-disable MD034 -->

{{% ingress %}}

Hvis du eier et e-postdomene, kan du velge å slå på en funksjon som heter *"catch all"*, som lar
deg motta alle meldinger som sendes til ditt domene, uavhengig av hva som står foran krøllalfa. Jeg
bruker dette selv på mitt eget domene.

{{% /ingress %}}

{{< img-lisens
    class="img-fluid"
    src="illustrasjonsbilde.jpg"
    alt="Illustrasjon. Grønn bakgrunn, to tegna hender holder en mobiltelefon. Ikoner som viser konvolutter flyr ut eller inn av  mobiltelefonen."
    type="Illustrasjonsbilde"
    artistlink="<https://bit.ly/3y6KnMH"
    artist="Mohamed Hassan"
    sourcelink="<https://bit.ly/3usohBT"
    source="Pixabay"
    lisenslink="https://pixabay.com/service/license/"
    lisens="Pixabay Lisence"
>}}

## "Normalt" oppsett

Hvis du ikke har "catch all" påskrudd, vil du måtte definere hvilke gyldige e-postadresser som
gjelder for ditt domene. Hvis noen prøver å sende en e-post til en utgått eller feilaktig adresse,
vil ikke denne komme frem.

I en bedrift vil det kanskje være normalt å opprette "post@domene.no" samt en e-postadresse til
alle ansatte, eksempelvis "navn.navnesen@domene.no". Hvis noe sendes til "posst@domene.no", vil
dette ikke komme frem.

## Hvis du skrur på "catch all"

Nå vil alle e-poster, som ikke allerede sendes til et en spesifikk e-postkonto, sendes til en
angitt e-postadresse. I eksemplet over, vil "postt@domene.no" komme frem til en angitt adresse. Det
har altså ingenting å si hva du skriver foran krøllalfasymbolet, alt kommer frem.

Også for gamle prosjekter, avdelinger, kampanjer og brukere, vil e-postadressen fortsatt være
aktiv, men pass på at dette ikke kommer i [konflikt med personvernet][datatilsynet].

## Hvorfor jeg bruker “catch all”

Jeg bruker funksjonen for å få økt kontosikkerheten til diverse brukerkontoer jeg har registrert på
internett, samt muligheten for å kunne avsløre om et firma har hatt datalekkasjer. Her er noen
eksempler på dette:

### Unike brukernavn på brukerkontoer

Du har sikkert lært at man skal ha et unikt passord på hver enkelt tjeneste man har registrert seg
på. For å øke kontosikkerheten ytterligere, vil et unikt brukernavn også ha en viss effekt. Jeg vil
nemlig ikke få en rekke innloggingsforsøk på min *faktiske* brukerkonto andre steder, som i noen
tilfeller kan låse kontoen.

Eksempel: Hos Facebook bruker jeg brukernavnet "facebook@pdog.no".

### Registrering av e-postadresser til engangsbruk

Hvis jeg trenger en e-postadresse til "engangsbruk", kan jeg bare lage en unik epostadresse til det
formålet. Hvis jeg senere ikke ønsker å få meldinger tilsendt, kan jeg bare blokkere
_mottakeradressen_, uavhengig av hva avsender måtte være.

Eksempel: Jeg vil melde meg på et nyhetsbrev hos Elkjøp for å oppnå en rabatt. Da kan jeg for
eksempel skrive "elkjop_nyhetsbrev_20200328@pdog.no". Da vet jeg nøyaktig hvilken avsender jeg skal
forvente, hva slags innhold jeg skal forvente, og hvilken dato jeg registrerte meg.

### Avsløring av lekkasjer og uautorisert dataoverføring

Det skjer fra tid til annen at firmaer jeg har brukerkontoer hos får sine systemer kompromittert,
som betyr at personlig informasjon som e-postadresser kan komme på avveie. Det kan også hende at
noen firmaer "selger" opplysningene på en uredelig måte. Ved å alltid kunne vite hvem som var ment
som avsender, kan jeg enkelt avsløre dette.

Eksempler:

- Jeg fikk søppelepost tilsendt til en e-postadresse jeg tidligere hadde brukt hos en
leiebiltjeneste jeg hadde leid bil av for lenge siden. - Datainnbrudd skjer hele tiden. Her er fire
eksempler fra [Foodora][foodora], [Microsoft][microsoft], [Marriot][marriot], [Rema
1000][rema1000].

## Ulemper med "catch all"

Selvfølgelig vil en person som målrettet går inn for å prøve mine kontoer, eller vil sende meg
uønsket e-post, klare å forstå strukturen i mine adresser, men de fleste lekkasjer er nok bare
situasjoner hvor man kjøper en stor database.

En annen ulempe er at man øker kompleksiteten av kontodetaljene, og det kan gjøre det vanskelig å
få gjenopprettet eller tilbakestilt kontoer hvis man har glemt det man opprinnelig skrev inn.

En tredje ulempe er at noen tjenester ikke tillater sitt eget firmanavn brukt i
brukernavn/e-postadresse.

Til slutt vil det også være hakket mer komplisert å snakke med bedrifter som krever at man sender
epost fra den adressen man har registrert for å få gjennomført endringer på kontoen. Man kan løse
det ved å enten endre e-postadressen midlertidig, eller få satt opp adressen som en “svar
fra”-adresse.

## Lær mer

Jeg lytter på en podkast som heter Mac Geek Gab, hvor de to programlederene tar opp en rekke
tekniske spørsmål fra lytterene sine. Sommeren 2017 sendte jeg inn et spørsmål hvor jeg forklarte
min e-poststrategi som beskrevet ovenfor, og spurte om de hadde noen innspill til dette. Du kan
lytte til programmet på deres nettsider: [Oh…Snap! – Mac Geek Gab 663][mgg] . Mitt spørsmål er det
første som tas opp, så du trenger ikke spole.

Har du en Gmail-konto kan noenlunde samme triks brukes der ved å legge til + etter adressen din.
Les mer her: [3 awesome Gmail address tricks to get more out of your email ID -
TheWindowsClub][thewindowsclub].

[datatilsynet]: https://www.datatilsynet.no/personvern-pa-ulike-omrader/personvern-pa-arbeidsplassen/innsyn-epost-filer/
[foodora]: https://www.vg.no/nyheter/innenriks/i/jdoO6A/lekkasje-av-kundedata-hos-foodora
[microsoft]: https://www.tek.no/nyheter/nyhet/i/0nl380/14-aar-av-microsofts-kundedata-laa-aapent-paa-nett
[marriot]: https://threatpost.com/millions-guests-marriott-data-breach-again/154300/
[rema1000]: https://norsis.no/kundedata-rema-1000-nye-app-ae-la-apent-tilgjengelig-2-uker/
[mgg]: https://www.macobserver.com/podcasts/macgeekgab-663/
[thewindowsclub]: https://www.thewindowsclub.com/gmail-address-tricks
