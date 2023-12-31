+++
title = "Beste praksis for QR-koder"
[menu]
main = {weight = 2, parent = "Personvern og sikkerhet" }
+++

<!-- markdownlint-disable MD033 -->

{{% ingress %}}

QR-koder har blitt populært å putte på diverse plakater, menyer, apparater o.l., men fører også med
seg en del utfordringer knytta til personvern og tilgjengelighet. Denne artikkelen er skrevet til
deg som publiserer og trykker opp QR-koder.

{{% /ingress %}}

{{< illustrasjonsbilde
 src="illustrasjon.png"
 alt="Illustrasjonsbilde som viser en mobiltelefon i forgrunnen"
>}}

Det er kjekt å bruke QR-koder, men det skaper også bekymringer i retning av sikkerhet og personvern.
*Illustrasjonsbilde, generert av DALL•E 3*.

{{< /illustrasjonsbilde >}}

<div class="container-fluid my-5">
  <!-- Full Width Best Practice Card -->
  <div class="card border-primary mb-3">
    <div class="card-header bg-primary text-white">Beste praksis</div>
    <div class="card-body text-primary">
      <h5 class="card-title">Ikke tving brukeren til å bruke QR-koder</h5>
      <p class="card-text">I forbindelse med QR-koden bør du alltid angi en forklaring for hvordan
      man kan besøke siden du ønsker uten å skanne koden med en mobiltelefon. Dette bør aller helst
      være en kortlenke som er lett å skrive inn, på et domene du kontrollerer.</p>
    </div>
  </div>
</div>

<div class="container-fluid my-5">

{{< hvorfor-ikke
 header="Manglende støtte operativsystemet"
 src="tip1.png"
>}}

Noen mobiltelefoner mangler (fremdeles) støtte for
QR-kodelesing i kameraappen på mobiltelefonen. Brukere må da henvende se til tredjeparts-apper, som
er upraktisk og tar tid å laste ned.

{{< /hvorfor-ikke >}}

{{< hvorfor-ikke
 header="Tredjepartsapper har sine problemer"
 src="tip2.png"
>}}

Dyre abonnementsløsninger, reklame som blokkerer innhold
eller forespørsel om tilganger som ikke er relevant for jobben den skal utføre.

{{< /hvorfor-ikke >}}

{{< hvorfor-ikke
 header="Teknisk kompetanse hos brukeren"
 src="tip3.png"
>}}

Noen mangler teknisk evne til å skanne QR-koder, og ev. til å laste ned en
tredjepartsapp for dette. Noen skjønner kanskje ikke hva en QR-kode er eller hvorfor den skal
skannes.

{{< /hvorfor-ikke >}}

{{< hvorfor-ikke
 header="Tenk på nettvett"
 src="tip4.png"
>}}

I forbindelse med QR-koden bør du alltid angi en forklaring for hvordan man kan besøke siden du
ønsker uten å skanne koden med en mobiltelefon. Dette bør aller helst være en kortlenke som er lett
å skrive inn, på et domene du kontrollerer.

Og i alle fall, ikke bruk kortlenketjenester som bit.ly. Les mer [her](../bitly).

{{< /hvorfor-ikke >}}

</div>
