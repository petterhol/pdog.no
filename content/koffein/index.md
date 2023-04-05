+++
title = "Hold Mac våken med koffein"
lastmod = 2021-04-07T22:00:00
[menu]
main = { weight = 9, parent = "Apple-tips" }
+++

{{% ingress %}}

Hvis du trenger å holde en Mac-datamaskin våken, for eksempel hvis du holder på med en
overføring eller et prosjekt, kan du tilføre "koffein".

{{% /ingress %}}

Det kan være verdt å nevne at man kan selvfølgelig kan justere hvor lang tid det tar før
Mac-datamaskinen slår seg av ved å gå til Systemvalg > Batteri. Å bruke kommandoene under
er ment som en midlertidig løsning.

Åpne Terminal og skriv inn følgende kommando:

{{% copy
 hiddentext="caffeinate"
 ident="kommando"
%}}
```caffeinate```{{% /copy %}}

Dette vil holde maskinen din våken helt til du avslutter den igjen.

Man kan for eksempel også sette en tidsgrense for hvor lenge maskinen skal være våken.
Finn antall sekunder (1 time er for eksempel 3600) skriv følgende:

{{% copy
 hiddentext="caffeinate -t 3600"
 ident="kommando"
%}}
```caffeinate -t 3600```{{% /copy %}}

For mer informasjon, kan du åpne brukermanualen til kommandoen:

{{% copy
 hiddentext="man caffeinate"
 ident="kommando"
%}}
```man caffeinate```{{% /copy %}}

For å avslutte kommandoen, kan man trykke Kontroll + C, eller bare avslutte Terminal-vinduet.

{{< tilbakemelding
	header="Fikk du bruk for dette?"
	id="koffein"
>}}
