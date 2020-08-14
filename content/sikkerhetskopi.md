+++
title = "Sikkerhetskopiering"
lastmod = 2020-08-12T12:00:00
[menu]
main = { parent = "Teknologi" }
+++

{{% ingress %}}

Hvis du har Apple-enheter, finner du her noen tips til hvordan du kan sikkerhetskopiere innholdet
på enhetene dine.

{{% /ingress %}}

## Begreper

- Sikkerhetskopi = backup (på engelsk)
- Innhold = alt du har av bilder, dokumenter, videoer, sanger og andre filer.
- Enhet = Samlebegrep for den fysiske tingen der innholdet er lagret,
  eksempelvis mobiltelefon, datamaskin, kamera, nettbrett.

***

## Hvorfor sikkerhetskopiere?

Alt du lagrer på digitale enheter bør ha en sikkerhetskopi. Det er mye som kan
gå galt, og hvis det gjør det, er det fint å kunne finne frem til en kopi av
innholdet ditt, slik at du ikke mister det for godt.

Her er noen eksempler på hva som kan skje:

- Du mister fysisk tilgang: Du kan bli frastjålet mobilen din, du kan miste
  kameraet ditt i en elv, du kan glemme igjen datamaskinen din på toget.
- Du ødelegger enheten din: Tenk deg at du setter deg på den bærbare
  datamaskinen, eller at du mister telefonen din i et basseng.
- Enheten din utsettes for ting utenfor din kontroll: En brann kan oppstå i
  hjemmet ditt, eller en naturkatastrofe kan inntreffe.
- Du mister tilgang på kontoen din: Enten kan du glemme passordet ditt, eller så
  kan kontoen bli låst av naturlige eller helt uforklarlige årsaker. Det hjelper
  ikke å klage, innholdet dine kan være tapt for alltid.
- Du sletter innholdet dine selv: For eksempel skriver du over alt du hadde på
  en harddisk fordi du trykket på feil knapp, eller så sletter du innholdet ditt
  i iCloud uten å vite at det bir slettet overalt.

Det er ingen tvil om at du må ha en, eller flere, sikkerhetskopier av innholdet ditt.

### Grunntanke: alt kan alltid gå tapt  

Bak bak all min tankegang rundt sikkerhetskopier er "alt kan alltid gå tapt". Det betyr at man
ikke skal stole på én teknologi eller plattform. Det handler ikke om at jeg har mistillit til
selskaper, plattformer, operativsystemer eller personer, men at menneskelige feil kan skje,
selskaper kan gå konkurs og så videre.
***
{{< egenrisk >}}

## 1. Start med iCloud

iCloud er et samlebegrep for noen skytjenester fra Apple. Hovedformålet er at man kan
*synkronisere* enkelte ting, som bilder, meldinger, kontakter med mer. Å synkronisere betyr at
alle endringer man gjør, oppdateres med en gang mot skyen. Alle enheter som er tilknyttet samme
iCloud-konto får endringen gjennomført med det samme.

Forvirrende nok inneholder iCloud noe som heter iCloud-sikkerhetskopi (for iPhone og iPad). Dette
inneholder appdata, Apple Watch-sikkerhetskopi, enhetsinnstillinger, Hjem-skjerm og
apporganisering, ringetoner og Visual Voicemail-passordet. iCloud-sikkerhetskopi blir IKKE
synkronisert, men det tas kopier automatisk hver natt så lenge enheten er koblet til strøm og
Wi-Fi[^icloudbackup].

Beste praksis: bruk iCloud til å synkronisere alt du kan, og ha på iCloud-sikkerhetskopi for
"resten". Slik skrur du det på:

**iPhone og iPad:**  

1. Innstillinger > Navnet ditt øverst > iCloud.
2. Sørg for at alt som kan skrus på (til grønt), er grønt.

**Mac:**  

1. Apple-logoen > Systemvalg > iCloud.
2. Sørg for at alt som kan være på, er på (krysset av).

Får du beskjed om at du ikke har nok plass på iCloud? Man kan kjøpe mer lagringsplass. Det er en
billig forsikring, og dessuten utrolig praktisk. Les mer om priser på [Lagringsabonnementer og
priser for iCloud (apple.no)](https://support.apple.com/no-no/HT201238).

## 2. iPhone og iPad: Koble til datamaskin

Den beste måten å få en grei kopi av innholdet fra en iPhone eller iPad er å bruke en datamaskin.

Siden iPhone ble lansert, har man alltid brukt programmet iTunes både for Windows og Mac. Hvis du
kjører den nyeste utgaven av macOS som heter Catalina, finnes ikke iTunes lengre, alt skjer i
Finder.

Beste praksis: Koble til datamaskinen og ta en sikkerhetskopi jevnlig, minst en gang i uken.
Denne artikkelen fra beskriver veldig greit hvordan man gjør det: [Slik sikkerhetskopierer du
iPhone, iPad og iPad touch (apple.no)](https://support.apple.com/no-no/HT203977#computer)

## 3. Sikkerhetskopier innholdet på datamaskinen

Nå som du har en kopi av alt innholdet fra dine mobile enheter på datamaskinen, kan du bare ta en
sikkerhetskopi av selve datamaskinen.

Poenget nå er at du tar en sikkerhetskopi til noe som _ikke_ ligger på datamaskinen din. Det
aller enkleste du kan gjøre er å kjøpe en ekstern harddisk (dette får du overalt på Elkjøp,
Power, Clas Ohlson osv.) Du kan også kjøpe mer avanserte sikkerhetskopisystemer.

For Mac anbefaler jeg å bruke den innebygde funksjonen *Time Machine*. Hvis du bruker Time
Machine, skjer dette automatisk så lenge disken er kobet til. Det er ingen fare å ha den koblet i
hele tiden mens du bruker maskinen.

Jeg har ikke så mye erfaring med Windows, men det ser ut som at det er en innebygget funksjon på
Windows 8 og oppover. Les artikkelen [Sikkerhetskopiere og gjenoprette PC-en din på Microsoft
Kundestøtte
(microsoft.no)](https://support.microsoft.com/nb-no/help/17127/windows-back-up-restore).

Beste praksis: Ta en sikkerhetskopi av datamaskinen jevnlig, minst hver uke. Slik setter du opp
Time Machine på Mac:

1. Koble til den eksterne harddisken. Det kan hende den må formateres først, i så fall les [Slik
   sletter du en disk på Mac (apple.no)](https://support.apple.com/no-no/HT208496).

2. Slå på Time Machine ved å gå til Apple-logoen > Systemvalg > Time Machine > Velg
   sikkerhetskopidisk. Velg den du har koblet til.

3. La maskinen stå koblet til strøm helt til første sikkerhetskopi er ferdig. Første gang tar
   alltid ganske lang tid, de resterende gangene tar det ikke noe særlig tid.

4. Når du nå har kopiert over innholdet på en harddisk, kan du vurdere å gjøre det for flere
   harddisker. Tenk deg at huset ditt brenner ned: da mister du kanskje både iPhone, Mac og
   harddisken. Hvis du har to harddisker, kan du plassere den andre hos noen du stoler på
   (venn/familie), på arbeidsplassen din, på hytta, i bilen og så videre.

***

## Alternativer til beste praksis

### Uten iCloud

Hvis du av ulike grunner ikke vil bruke iCloud, kan du hoppe over det og bare koble til en
datamaskin. Ulempen da er at du er helt avhengig av nylig sikkerhetskopi. Jeg ville minst kopiert
over innholdet to ganger i uka, helst oftere.

#### Uten datamaskin

Hvis du ikke har en datamaskin, kan du kopiere deler av innholdet ditt til diverse
internettjenester. Bilder er lett, bare last ned og bruk Google Photos, Dropbox, OneDrive, Min
Sky (hvis du er Telenor-kunde) eller en annen tjeneste.

#### Uten ekstern harddisk

Jeg vil bare understreke at det ikke er mulig å ta en sikkerhetskopi til en harddisk på
datamaskinen. Hele poenget er at den innebygde harddisken *kan* bli ødelagt. En enkel, ekstern
harddisk er ikke dyrt og er en billig forsikring. Alternativet er å bruke skytjenester som
Backblaze eller JottaCloud.

***

## Personlig hjelp

Siden jeg brenner for at folk bør ha en sikkerhetskopi, og jeg normalt ikke har noe imot å hjelpe
folk som trenger det uten å forvente noe tilbake, kan jeg *kanskje* hjelpe deg med å sette opp en
fungerende sikkerhetskopi. Det er helt gratis, men ikke ha noen forventninger til hva jeg kan
gjøre og når jeg kan gjøre det.

Hvis du allerede har mistet data? Slutt å bruke det som inneholdt dataen du mistet. Det er
sannsynlig at dataen har gått tapt for alltid, men jeg er alltid åpen for å prøve.

Ellers er det mye profesjonell hjelp å få. Apple og Microsoft har sannsynligvis gode løsninger
for å komme i kontakt med kundestøtte. Mange elektronikkbutikker kan sikkert også hjelpe, men
noen kan kanskje ta betalt for det.

[^icloudbackup]: https://support.apple.com/no-no/HT207428
