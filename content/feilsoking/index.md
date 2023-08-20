+++
title = "Generell feilsøking av problemer av duppeditter"
[menu]
main = { weight = 9, parent = "Apple-tips" }
+++

{{% ingress %}}

Hvis du står ovenfor en situasjon hvor du må hjelpe noen å feilsøke et teknisk problem på det jeg
her kaller for "duppeditter" (det være seg datamaskiner, mobiltelefoner, fjernsynsapparat,
spillkonsoller, smartklokker og så videre), kan det være lurt å følge
noen grunnleggende prinsipper for hvordan du skal gå fram. I denne artikkelen tar jeg for meg noen
grunnleggende strategier og metoder for å feilsøke generelle problemer.

{{% /ingress %}}

Strategiene og metodene som presenteres her skal ikke brukes i en gitt rekkefølge, og kan utføres
helt, delvis eller ikke i det hele tatt. En erfaren feilsøker vil som regel bruke flere metoder
samtidig, for å komme effektivt fram til riktig svar. Noen ganger kan
det være lettere å bare ta en omstart av en datamaskin, enn å prøve å forstå brukerens dypeste
tanker og følesler knyttet til hvorfor akkurat dette er et problem.

I denne artikkelen brukes begrepet _brukeren_ om personen som du hjelper å feilsøke noe med.

#### Still gode spørsmål – ikke ta noe for gitt

Noe av det letteste å gjøre når man feilsøker et teknisk problem, er å ta for gitt at noe er sant
uten å ha undersøkt det. Avhengig av hvem man prater med, er det heller ikke slik at man kan ta for
gitt at noe noen _sier_ er sant.

La oss ta et enkelt eksempel hvor du stiller et spørsmål eller lurer på noe : «er telefonen koblet
til det trådløse nettet»? Hvis du spør brukeren av telefonen om dette, vil vedkommende kanskje si
«ja», selv om svaret i realiteten er «nei». Her er noen eksempler på hvorfor du kan få feil svar:

- brukeren vet kanskje ikke hva det vil si å være koblet på et trådløst nett
- brukeren vil kanskje ta det for gitt at så lenge telefonen ikke er koblet til noen kabler, at den
er på trådløst nett
- brukeren vil kanskje mangle forståelse av forskjellen på et «hjemmenettverk» og «mobilnettverk»
- brukeren vet kanskje at mobilen vanligvis er koblet til det trådløse hjemmenettverket, men
tilkoblingen kan ha falt ut av en eller annen grunn

Ikke spør – bruk heller tiden på å sjekke eller still gode spørsmål som hjelper deg å komme fram
til det svaret du trenger.

Et annet godt eksempel er hvor man har spurt om brukeren har startet maskinen på nytt, og du får nok
en gang et feilaktig «ja»: kanskje brukeren tror at å lukke lokket på den bærbare maskinen
er det samme som å «starte på nytt»?

Jeg har laget en artikkel som hjelper deg å sjekke hvor lenge en Windows- eller Mac-datamaskin har
vært påskrudd (og dermed også verifisere om vedkommende snakker sant eller ikke):
[Kontroller siste omstart av en datamaskin](../omstart).

#### Noen ganger kan selv de enkleste tekniske begreper være for meget

Dette kan være vanskelig, både å forstå og holde seg unna, men av og til vil begreper fra
dataverdenen være uforståelig eller misforstått av brukeren.

Jeg har flere ganger vært borti at brukere tror at en «omstart» eller på engelsk «restart» betyr å
slette alt på enheten og sette den opp på nytt. Når man da ber de om å ta en omstart for å se om det
løser problemet, risikerer man at brukeren motsetter seg dette i frykt mot å miste viktig innhold.

Vi omgir oss også med begreper som «Wi-Fi», «3G/4G/5G», «hjemskjermen», «kode», «SIM-kort» og så
videre, som brukeren kanskje ikke vet hva betyr, eller har misforstått.

En god løsning rundt dette kan heller å la brukeren fortelle ved å stille gode spørsmål:

- hva ser du på skjermen?
- hva skjedde da du gjorde …?
- hva bruker å skje når du …?
- hvordan vil du beskrive ikonet du trykker på?

Da får man ofte god nok informasjon til å gå videre.

#### Isolasjon av problemet

Ved å _isolere_ problemet til et enkelt komponent, finner du lett ut hvor du skal begynne, eller
kanskje isoleringen i seg selv løser problemet. Her går man løs på komponent for komponent, for å
finne ut om det er noe feil med det spesifikke komponentet. I tillegg er det fint å ha noe man vet
fungerer. Vi kommer tilbake til dette i eksemplene.

La oss ta et enkelt eksempel: «telefonen lader ikke». Siden vi ikke skal anta noe, spør vi først om
telefonen for øyeblikket er påskrudd, eller om den har mistet all batterikapasitet. En
avslått/strømløs telefon er ikke akkurat til hjelp for å finne feilen. Telefonen i dette eksemplet
er på.

Da kan vi begynne isoleringen:

- Vet vi at stikkontakten fungerer? Test med noe man _vet_ fungerer når det er koblet til
stikkontakten, for eksempel en lampe, eller til en stikkontakt en lampe allerede står koblet i.
- En «lader» består ofte av to forskjellige komponenter: en strømadapter og en kabel. Å koble disse
fra hverandre og teste på noe annet kan være lurt. En løs kabel kan kobles i en datamaskin, mens det
finnes sikkert noe annet som strømadapteren kan kobles inn i.
- Hvis både kabel og strømadapter fungerer fint, kan vi deretter prøve å lade telefonen med en annen
lader. Ingen respons? Da er det kanskje noe feil med telefonen.

Og slik fortsetter man til man har funnet ut hvor feilen kan ligge. Ved å bytte ut de fysiske
komponentene, utelukker vi de enkleste «selvfølgeligheter».

*Denne artikkelen vil etterhvert oppdateres med flere strategier og metoder.*
