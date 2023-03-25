+++
title = "Bilregnskap"
[menu]
main = { weight = 9, parent = "Forbruker" }
+++

{{% ingress %}}

Å eie en bil koster langt mer penger enn bare drivstoffet og bompenger. Man må kalkulere inn ting
som verkstedbesøk, serviceintervaller, oljeskift, diverse løsøre i bilen, avgifter og forsikringer,
dekkbytter og nye dekk, fergeregninger og mye mer.

{{% /ingress %}}

Dette løpende bilregnskapet søker å samle all data som omhandler bilens økonomi, og gir bilens
eier eller bruker en komplett oversikt over alle transaksjoner og forskjellige kalkulerte verdier.
På denne måten kan du for eksempel finne bilens faktiske pris totalt, per dag, per kilometer,
og mye mer.

## Funksjoner

### Drivstoff

For alle drivstoffyllinger, fyller du inn følgende informasjon:

- dato
- beløp for fylling
- kilometerstand ved fylling
- antall fylte liter

Drivstoffmodulen vil regne ut følgende:

- antall kilometer kjørt siden forrige fylling
- antall liter per kjørte norske mil
- antall dager siden forrige fylling
- kroner brukt per dag på tanken
- kilometer kjørt per dag
- kroner per liter

I tillegg farvekodes antall liter per kjørte norske mil for å gi et inntrykk av hvor økonomisk
kjøringen har vært. Grønne tall er "gode" tall, gule er midt på treet og røde er "dårlige" tall.

### Utgifter

For alle utgifter, fyller du inn følgende informasjon:

- post (det vil si kategori)
- beskrivelse (fritekst)
- dato for utgiften
- kreditor (hvem det er betalt til)
- antall kroner betalt

Alle tall fylles inn som positive tall, bortsett fra situasjoner hvor bilen selges eller får
et form for kontantoppgjør eller forsikringsoppgjør, da bruker du negative tall.

Følgende poster kan du for eksempel bruke:

- innkjøp (alle utgifter relatert til at du har kjøpt inn bilen, som salgssummen, omregistrering,
den første tanken med drivstoff, oppgjør etter reklamasjoner på kjøp)
- fast (forsikringer, årsavgifter)
- vedlikehold (oljeskift, AC-gass, drivstoffilter, dekkjøp, nye bremser)
- salg (inntekter og utgifter relatert til salget av bilen)

Du kan selv velge hvilke kategorier du bruker og hva de skal inneholde. Det viktigste er at det gir
mening for deg når du skal se på totaloppsummeringene.

### Dekningsposter

| **Kolonnefelt**      | **Formatering fra regnearket** | **Formler**                                                                                                                                                                                               |
|----------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```Dato```           | Dato, formatert åååå-mm-dd     | Ingen, fylles ut av bruker                                                                                                                                                                                |
| ```Kroner (kr)```    | Tall, formatert ### ###,##     | Ingen, fylles ut av bruker                                                                                                                                                                                |
| ```Kilometer (km)``` | Tall, formatert ### ### ###    | Ingen, fylles ut av bruker                                                                                                                                                                                |
| ```Liter (l)```      | Tall, formatert ###,##         | Ingen, fylles ut av bruker                                                                                                                                                                                |
| ```km/kjørt```       | Tall, formatert ### ###        | hvis det er verdi på radens kilometer-kolonne:<br>antall kilometer på gjeldende rad minus antall kilometer på raden over<br><br>hvis ikke:<br>skriv tallet 0                                              |
| ```l/100km```        | Tall, formatert av formel      | hvis det er verdi på radens liter-kolonne:<br>avrund følgende verdi med to desimaler:<br>del følgende svar på 100:<br>antall liter delt på km/kjørt<br><br>hvis ikke:<br>hold cellen blank                |
| ```kr/l```           | Tall, formatert av formel      | hvis det er verdi på radens liter-kolonne:<br>avrund følgende verdi med to desimaler:<br>del kroner på liter<br><br>Hvis ikke:<br>hold cellen blank                                                       |
| ```dager```          | Tall, formatert av formel      | hvis det er verdi på radens liter-kolonne (tilfeldig kolonne):<br>regn ut avstanden mellom følgnede to datoer:<br>radens datokolonne og raden over sin datokolonne<br><br>hvis ikke:<br>hold cellen blank |
| ```dager/km```       |                                |                                                                                                                                                                                                           |	