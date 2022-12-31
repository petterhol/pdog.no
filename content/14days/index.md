+++
title = "Justering av ukevisning i Kalender"
lastmod = 2021-04-07T22:00:00
[menu]
main = { weight = 9, parent = "Apple-tips" }
+++

{{% ingress %}}

Hvis du bruker appen Kalender på Mac, kan du justere antall dager som vises i ukevisningen utover
de to valgene på 5 og 7 dager som er standard.

{{% /ingress %}}

{{< img-caption
  figure-class="float"
    class="rounded"
    src="bilde.png"
    alt="Skjermbilde av kalender på Mac som viser 14 dager om gangen"
    img-caption="Skjermbilde av kalender på Mac som viser 14 dager om gangen"
  >}}

Følgende kommando i Terminal gir deg mulighet til å justere antall dager. Bytt ut 0 med antall
ønskede dager:

{{% copy
 hiddentext="defaults write com.apple.iCal n\ days\ of\ week 0"
 ident="kommando"
%}}
```defaults write com.apple.iCal n\ days\ of\ week 0```{{% /copy %}}

Personlig kjører jeg en 34-tommers bredskjerm med 14 dager i ukevisning.

For å endre tilbake til standardvisningen, gjør en av følgende:

* Kjør samme kommando hvor ```x``` er ```5``` eller ```7```.
* Gå til Kalender > Valg > Generelt > Dager per uke og endre dette til enten ```5``` eller ```7```.
