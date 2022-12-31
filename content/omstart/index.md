+++
title = "Kontroller siste omstart av en datamaskin"
lastmod = 2021-04-07T22:00:00
[menu]
main = { weight = 9, parent = "Apple-tips" }
+++

{{% ingress %}}

Et viktig steg i generell isolering og feilsøking av problemer på en datamaskin er å
starte maskinen på nytt. Noen brukere har ikke en forståelse av hvordan man gjør det, og
derfor kan det være nyttig å sjekke hvor lenge en datamaskin har vært påskrudd. Her lærer
du hvordan du gjør dette på Mac og Windows.

{{% /ingress %}}

### Mac

#### Alternativ 1 – Systeminformasjon

1. Åpne Finder, trykk på Gå og velg Verktøy.
2. Åpne appen "Systeminformasjon".
3. I vinduet som åpner seg, velg "Programvare" på venstre side.
4. "Tid siden oppstart" gir deg svaret du er på jakt etter.

#### Alternativ 2 – Terminal

1. Åpne Finder, trykk på Gå og velg Verktøy.
2. Åpne appen "Terminal".
3. I vinduet som åpner seg, skriv ``uptime`` og trykk på returknappen
(enter, linjeskift).
4. Svaret på neste linje sier hvor lenge maskinen har vært påskrudd.

### Windows

#### Alternativ 1 – Oppgavebehandling

1. Åpne Windows-menyen og søk på "Oppgavebehandling". Åpne appen.
2. Velg fanen "Ytelse".
3. Velg "Mer info" om nødvendig.
4. Varigheten som vises under "Oppetid" er svaret du er på jakt etter.

#### Alternativ 2 – Ledetekst

1. Åpne Windows-menyen og søk på "cmd". Åpne appen Ledetekst.
2. I vinduet som åpner seg, skriv ``systeminfo`` og trykk på returknappen
(enter, linjeskift).
3. En del informasjon vises om maskinen, herunder "System boot time".
