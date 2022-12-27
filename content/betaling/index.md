+++
title = "Digital ID og betalingsmetoder i Norge"
[menu]
main = { parent = "Forbruker", weight = 1 }
+++

{{% ingress %}}

Jeg fant ingen gode artikler som oppsummerte dette på en god måte, så jeg bestemte meg for å skrive om det på egenhand. Denne artikkelen tar for konsepter og forskjeller på betalingskort, spesielt i det norske markedet.

{{% /ingress %}}

### Betalingskort

##### Debitkort – koblet direkte mot en bankkonto
I Norge tilbyr mange banker dagligbanktjenester, som inkluderer en brukskonto og et debitkort. Når du bruker kortet, reserveres et beløp på kontoen din og din disponible saldo minsker med en gang.

I Norge tilbys følgende debitkort:

---

{{< img
	class="rounded"
	src="bankaxept.svg"
	alt="tekst"
	width="100"
	align="right"
	padding="10"
>}}

###### BankAxept
Som et samarbeidsprosjekt mellom alle norske banker med dagligbanktjenester finnes BankAxept som tilbys i norske kortterminaler. Hadde et prosjekt med betaling på internett (BankAxess), som ble nedlagt 1. desember 2022.

---

{{< img
	class="rounded"
	src="visa-debit.svg"
	alt="tekst"
	width="100"
	align="right"
	padding="10"
>}}

###### VISA Debit
Tilbys av de aller fleste norske banker med dagligbanktjenester. Tilbys i kortterminaler over hele verden, samt betaling på internett.

---

{{< img
	class="rounded"
	src="visa-electron.svg"
	alt="tekst"
	width="100"
	align="right"
>}}

###### VISA Electron
Tilbys av flere norske banker med dagligbanktjenester. Kan bare brukes i tilfeller hvor det er mulig å sjekke saldo og trekke pengene direkte, det vil si uten fare for å overtrekke kortet. Kan ikke brukes på internett. 

---


{{< img
	class="rounded"
	src="mastercard-debit.svg"
	alt="tekst"
	width="100"
	align="right"
>}}

###### Mastercard debit
Tilbys av noen norske banker med dagligbanktjenester, som Handelsbanken og N26. Tilbys i kortterminaler over hele verden, samt betaling på internett.

---

{{< alert
	color="dark"
	text="left"
	header="BankAxept og VISA/Mastercard på samme kort?"
>}}

Det er helt vanlig i Norge å tilby BankAxept og enten VISA Debit/Electron eller MasterCard Debit på samme kort. Butikkene som tar betalt med kort, må betale et gebyr per transaksjon (ofte et fastledd + prosent av summen) til en leverandør av korttjenester.
BankAxept får man relativt billig sammenliknet med VISA og MasterCard. En norsk betalingsterminal som støtter BankAxept og VISA, vil velge BankAxept.

{{< /alert >}}

---

##### Kredittkort – betale på kreditt og få faktura i etterkant
Banken vil gjennomføre en kredittvurdering og gi deg en kredittgrense som begrenser hvor mye du kan handle for. Forbruket får du en faktura for i etterkant, gjerne neste kalendermåned.

---

{{< img
	class="rounded"
	src="mastercard-debit.svg"
	alt="tekst"
	width="100"
	align="right"
>}}

###### VISA Credit
Flere norske banker tilbyr VISA Credit so 

---

{{< img
	class="rounded"
	src="mastercard-debit.svg"
	alt="tekst"
	width="100"
	align="right"
>}}

###### MasterCard Credit

---

{{< img
	class="rounded"
	src="mastercard-debit.svg"
	alt="tekst"
	width="100"
	align="right"
>}}

###### American Express




Mange kjenner American Express som AmEx. Kortet ble tilbudt gjennom DNB i lang tid frem til 2017, men deretter gjort om til sin egen, selvstedige enhet. Ved lanseringen ble det tilbudt som et faktureringskort, hvor hele gjelden måtte betales ned når regningen kom (i motsetning til "vanlige" kredittkort).

###### Kredittkort fra energistasjoner
Enkelte energistasjoner tilbyr kredittkort som bare gjelder for tjenester for den energistasjonkjeden. Noen av disse kortene igjen kan være et "vanlig" kredittkort (fra for eksempel VISA eller MasterCard), men det kan også være helt rene kort som bare fungerer til betaling av drivstoff, bilvask, med mer.

### Betalingsmåter for betalingskort

Det finnes flere måter å belaste et betalingskort på.

#### Betaling ved å oppgi kortinformasjon
Ofte på internett, eller over telefon, og av og til på en fysisk kortterminal, kan man betale ved å oppgi sin kortinformasjon. Denne består av følende:

- korttype
- kortnummer (16 siffer)
- utløpsmåned og -år (mm/åå)
- sikkerhetskode (3 eller 4 siffer)
- navn på kortet
- helt eller delvis adresseinformasjon

Ikke alle utsalgssteder ber om all informasjon. Norske utstedere ber som regel bare om de fire øverste.

Noen ganger blir man sendt videre til et ekstra autentiseringssteg kjent som 3D Secure. Her ber banken deg identifisere at det er du som gjennomfører kjøpet.

BankAxept støtter ikke denne typen betalinger, noe som gjør at hvis man vil betale for fysiske varer i en fysisk butikk via en nettbutikk eller app, vil utsalgsstedet tilby VISA eller MasterCard til en høyere transaksjonspris.

#### Betaling ved å bruke magnetstripe, chip eller kontaktløs betaling på fysiske plastkort
På fysiske utsalgssteder kan man bruke enten magnetstripen, chippen eller kontaktløs betaling ("tæpp") for å autentisere kjøpet. Magnetstripe og chip vil alltid be om at man taster inn PIN-koden. For kontaktløse betalinger er det ofte en grense for hvor stort et kjøp kan være før man ber om PIN, og av og til ber man om PIN uansett som en tilfeldig sjekk.

#### Betaling med mobil, smartklokke med mer
I Norge er det tilgjengelige tjenester for å betale direkte med mobiltelefoner, smartklokker osv. Dette er tjenestene Apple Pay, Google Pay, Garmin Pay og Fitbit Pay.

## Vipps
Vipps tilbyr 

- betaling direkte fra konto for person-til-person-betalinger
- betaling fra betalingskort for person-til-person-betalinger
- betaling fra betalingkort for person-til-bedrift-betalinger


## Andre ting
### BankID
BankID er utelukkende en autentiseringsmetode, og har ikke noe med betalingen i seg selv å gjøre. Du blir kanskje bedt å "godkjenne" en betaling med BankID, men det er bare for å vite at det er du som gjør betalingen.