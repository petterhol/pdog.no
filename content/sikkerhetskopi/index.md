+++
title = "Beste praksis for sikkerhetskopi av Apple-enheter"
linktitle = "Beste praksis for sikkerhetskopi"
aliases = [
    "backup",
]
[menu]
main = { weight = 3, parent = "Apple-tips" }
+++

<!-- markdownlint-disable MD033 -->

{{% ingress %}}

I denne artikkelen forklarer jeg først generelt om sikkerhetskopiering for alle,
og deretter går jeg detaljert til verks for å forklare hvordan en person som minst har en
iPhone eller iPad og Mac burde sikkerhetskopiere.

{{% /ingress %}}

### Hva er en sikkerhetskopi og hvorfor bør du ha det?

En sikkerhetskopi er å lagre innhold på flere steder, med den hensikt å kunne hente det tilbake
hvis noe går galt med enhetene dine. Her er noen eksempler på hva som kan skje:

{{< kort-align
 width="30"
 align="right"
 header="Ord og uttrykk i denne artikkelen"
>}}

<p><b>Sikkerhetskopi</b>: Backup (på engelsk)</p>
<p><b>Innhold</b>: Alt du har av bilder, dokumenter, videoer, sanger og andre filer.</p>
<p><b>Enhet</b>: Samlebegrep for den fysiske tingen der innholdet er lagret,
eksempelvis mobiltelefon, datamaskin, kamera, nettbrett.</p>

{{< /kort-align >}}

- Du mister *fysisk tilgang*: Du kan bli frastjålet mobilen din, du kan miste
  kameraet ditt i en elv, du kan glemme igjen datamaskinen din på toget.
- Du *ødelegger enheten* din: Tenk deg at du setter deg på den bærbare
  datamaskinen, eller at du mister telefonen din i et basseng.
- Enheten din utsettes for *ting utenfor din kontroll*: En brann kan oppstå i
  hjemmet ditt, eller en naturkatastrofe kan inntreffe.
- Du mister tilgang på *kontoen din*: Enten kan du glemme passordet ditt, eller så
  kan kontoen bli låst av naturlige eller helt uforklarlige årsaker. Det hjelper
  ikke å klage, innholdet dine kan være tapt for alltid.
- Du sletter innholdet dine *ved en feil*: For eksempel skriver du over alt du hadde på
  en harddisk fordi du trykket på feil knapp, eller så sletter du innholdet ditt
  i iCloud uten å vite at det bir slettet overalt.
  
{{< alert
 color="dark"
 align="center"
 header="Grunnleggende holdning: Alt kan alltid gå tapt"
>}}

Du må alltid ha som utgangspunkt at alt kan gå galt til en hver tid. Du burde ikke stole på én
eller ett enhet, tjeneste, selskap, fysisk lokasjon eller person. Alle kan gjøre feil, og uforutsette
ting skjer hele tiden.

{{< /alert >}}

***

### 1. Sørg for at iCloud er korrekt satt opp på alle enheter

iCloud er et samlebegrep for noen skytjenester fra Apple. Hovedformålet er at man kan
*synkronisere* innhold, som bilder, meldinger, kontakter med mer. Å synkronisere betyr at
alle endringer man gjør, oppdateres med en gang mot skyen. Alle enheter som er tilknyttet samme
iCloud-konto får endringen gjennomført med det samme.

Forvirrende nok inneholder iCloud noe som heter iCloud-sikkerhetskopi (for iPhone og iPad). Dette
inneholder appdata, Apple Watch-sikkerhetskopi, enhetsinnstillinger, Hjem-skjerm og
apporganisering, ringetoner og Visual Voicemail-passordet. iCloud-sikkerhetskopi blir IKKE
synkronisert, men det tas kopier automatisk hver natt så lenge enheten er koblet til strøm og
Wi-Fi [^icloudbackup].

Beste praksis: bruk iCloud til å synkronisere alt du kan, og ha på iCloud-sikkerhetskopi for
"resten". Slik skrur du det på:

**iPhone og iPad:**  

1. Innstillinger > Navnet ditt øverst > iCloud.
2. Sørg for at alt som kan skrus på (til grønt), er skrudd på.

**Mac:**  

1. Apple-logoen > Systeminnstillinger (eller Systemvalg) > iCloud.
2. Sørg for at alt som kan være på, er på (krysset av).

Får du beskjed om at du ikke har nok plass på iCloud? Man kan kjøpe mer lagringsplass. Det er en
billig forsikring, og dessuten utrolig praktisk. Les mer om priser på [Lagringsabonnementer og
priser for iCloud (apple.no) {{< ext >}}](https://support.apple.com/no-no/HT201238).

### 2. iPhone og iPad: Koble til datamaskin

Beste praksis: Koble til datamaskinen og ta en sikkerhetskopi jevnlig, minst en gang i uken.
Denne artikkelen fra beskriver veldig greit hvordan man gjør det: [Slik sikkerhetskopierer du
iPhone, iPad og iPad touch (apple.no) {{< ext >}}](https://support.apple.com/no-no/HT203977#computer).

### 3. Sikkerhetskopier innholdet på datamaskinen

Nå som du har en kopi av alt innholdet fra dine mobile enheter på datamaskinen, kan du bare ta en
sikkerhetskopi av selve datamaskinen.

Poenget nå er at du tar en sikkerhetskopi til noe som *ikke* ligger på datamaskinen din. Det
aller enkleste du kan gjøre er å kjøpe en ekstern harddisk (dette får du overalt på Elkjøp,
Power, Clas Ohlson osv.) Du kan også kjøpe mer avanserte sikkerhetskopisystemer.

Mac har en innebygget programvare som hetre *Time Machine*. Hvis du bruker Time
Machine, skjer dette automatisk så lenge disken er kobet til. Det er ingen fare å ha den koblet i
hele tiden mens du bruker maskinen.

Beste praksis: Ta en sikkerhetskopi av datamaskinen jevnlig, minst hver uke. Slik setter du opp
Time Machine på Mac:

1. Koble til den eksterne harddisken. Det kan hende den må formateres først, i så fall les [Slik
   sletter du en disk på Mac (apple.no) {{< ext >}}](https://support.apple.com/no-no/HT208496).

2. Slå på Time Machine ved å gå til Apple-logoen > Systeminnstillinger (eller Systemvalg) >
Time Machine > Velg sikkerhetskopidisk. Velg den du har koblet til.

3. La maskinen stå koblet til strøm helt til første sikkerhetskopi er ferdig. Første gang tar
   alltid ganske lang tid, de resterende gangene tar det ikke noe særlig tid.

4. Når du nå har kopiert over innholdet på en harddisk, kan du vurdere å gjøre det for flere
   harddisker. Tenk deg at huset ditt brenner ned: da mister du kanskje både iPhone, Mac og
   harddisken. Hvis du har to harddisker, kan du plassere den andre hos noen du stoler på
   (venn/familie), på arbeidsplassen din, på hytta, i bilen og så videre.

Jeg vil bare understreke at det ikke er mulig å ta en sikkerhetskopi til en harddisk på
datamaskinen. Hele poenget er at den innebygde harddisken *kan* bli ødelagt. En enkel, ekstern
harddisk er ikke dyrt og er en billig forsikring.

Hvis man vil ha ytterligere kopier, kan man også abonnere på spesifikke skytjenester for
sikkerhetskopiering. Jeg bruker selv [Backblaze {{< ext >}}](https://www.backblaze.com), og jeg
har hørt gode ord om [JottaCloud {{< ext >}}](https://www.jottacloud.com/nb/).

[^icloudbackup]: https://support.apple.com/no-no/HT207428

{{< tilbakemelding
header="Ting endrer seg, har du oppdaget noe som ikke stemmer, eller har du flere tips?"
id="sikkerhetskopi"
>}}
