+++
title = "Direktemanipulering av tekst"
lastmod = 2021-04-07T22:00:00
[menu]
main = { weight = 10, parent = "Apple-tips" }
+++

{{% ingress %}}

Hvis du vil manipulere på tekst på en nettside i nettleseren din, kan du åpne inspektøren
og gjøre endringer direkte i koden. I tillegg kan man bruke document.designMode = "on"
for å redigere i What You See Is What You Get (WYSIWYG)-format.

{{% /ingress %}}

Denne guiden gjelder Safari på macOS Monterey, men kan sannsynligvis gjelde andre versjoner
og nettlesere.

Du må bruke Konsoll for å slå på denne funksjonen, som du kan aktivere på en av tre måter:

- Trykk på Utvikle i menylinjen, og velg Vis JavaScript-konsoll. Hvis du ikke har utvikle
i menylinjen, gå til Safari > Valg > Avansert og skru på "Vis Utvikle-menyen i menylinjen".
- Bruk tastatursnarveien tilvalg-kontroll-I.
- Kontroll-klikk hvor som helst på nettsiden, velg Inspiser element og velg Konsoll.

Når du er i Konsoll, kan du skrive inn følgende kommando nederst på siden:

{{% designmodeon %}}

Du kan reversere kommandoen ved å endre ```"on"``` til ```"off"```, eller bare
gå ut av nettsiden.
