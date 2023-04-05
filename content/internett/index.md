+++
title = "Sjekk av internettforbindelsen"
[menu]
main = { weight = 9, parent = "Andre prosjekter" }
+++

{{% ingress %}}

Du har nå havnet på en eksperimentell side hvor jeg prøver å lage en side som sjekker
internettforbindelsen til brukeren som laster siden.

{{% /ingress %}}

{{< confirmation-code >}}

Tallet du ser på "Nåværende kode" gjør følgende:

1. Henter nåværende UTC-klokkeslett fra worldtimeapi.org
2. Henter differansen siden Epoch
3. Oppdaterer på intervall hvert trettiende sekund.
4. Ganger tallet med 7919357 (tilfeldig tall).
5. Viser bare de siste seks sifrene i tallet som blir generert.

Tallet du ser under "Forrige kode" gjør det samme, bare at den viser forrige intervall.

Tallene oppdaterer seg ikke automatisk (enda). Du må derfor manuelt oppdatere nettleseren
for å få siste oppdatering av tallene.

Formålet med siden er å tilby en tjeneste for enhver person som hjelper en annen med å
absolutt verifisere at enheten er på internett. Siden koden er kjent for begge enheter,
kan man lett verifisere at man ser på samme kode i samme intervall.

Under følger noen ofte stilte spørsmål om tjenesten.

Spørsmål: Hvorfor henter du ikke bare tiden fra maskinen?  
_Svar: Fordi maskintid kan manipuleres, det kan ikke internettiden fra API-et._

Spørsmål: Hvorfor spør man ikke bare den man hjelper om de har internett?  
_Svar: Hvis du hjelper noen som ikke er teknisk kompetent, vil de ikke kunne svare
pålitelig på dette spørsmålet. Du burde alltid verifisere._

Spørsmål: Hvorfor ber du ikke den man hjelper å gå inn på en tilfeldig nettside?  
_Svar: Hvis du hjelper noen som ikke er teknisk kompetent, kan de gå inn på en side som
ikke er en internettside, en side de har åpen som en fane, en side som er mellomlagret
eller liknende. Du burde alltid verifisere._

Spørsmål: Hvorfor ber du ikke den man hjelper om å for eksempel bruke Terminal eller
Ledetekst?  
_Svar: Hvis den du hjelper ikke er teknisk kompetent, vil du gjøre frykten deres for
datamaskiner og teknologi enda verre._

Jeg vil fortsette å utvikle tjenesten. Planen er å ta den ut fra pdog.no og inn
på et eget domene, med egne landingssider for teknisk kompetente og for de du hjelper.
Men i sin enkleste form er denne siden tilstrekkelig nå.

Takk til Eivind Hystad og Stig Johan Berggren for hjelp til utvikling av tjenesten.

{{< tilbakemelding
	header="Vil du hjelpe meg å utvikle denne tjenesten, eller har du noen tilbakemeldinger?"
	id="internettsjekk"
>}}