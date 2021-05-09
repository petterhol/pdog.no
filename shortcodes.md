# Om denne siden

Her legger jeg inn alle Markdown-malene til shortcodes jeg bruker på nettsiden, slik at jeg lett kan finne dem igjen. Variabler merkes med fem x-sympboler: ```xxxxx``` og vi bruker
[Code and Syntax Highlighting](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code-and-syntax-highlighting)
for å gjerde inn koden.

## Copy

Formål: Legger til en "Kopier"-knapp til hørye for ønsket tekst.

Variabler:
- hiddentext: den faktiske verdien som skal kopieres til utklippstavlen.
- ident: en unik identifiseringsverdi, for Javascript-koden til å vite hvilken verdi som skal kopieres.

```html
{{% copy
	hiddentext="xxxxxx"
	ident="xxxxxx"
%}}
xxxxxx {{% /copy %}}
```

## img-lisens

Formål: Legger til et bilde, samt lisensinformasjon under.

Variabler:
- class: img-class, normalt "img-fluid"
- src: kilde til bildet
- alt: alternativ tekst
- type: kategorisering av hva verket er for noe, eksempel bilde
- aristlink: lenke til kunstner nettside
- artist: navnet på kunstner
- sourcelink: hvor verket er hentet fra
- source: navnet på stedet verket er hentet fra
- lisenslink: lenke til lisensinformasjon
- lisens: beskrivelse av lisensen

```html
{{< img-lisens
	class="xxxxx"
	src="xxxxx"
	alt="xxxxx"
	type="xxxxx"
	artistlink="xxxxx"
	artist="xxxxx"
	sourcelink="xxxxx"
	source="xxxxx"
	lisenslink="xxxxx"
	lisens="xxxxx"
>}}
```

## Img-caption-link

Formål: Legger til et klikkbart bilde med bildetekst i grå tekst. Kan både brukes til ekstenre nettsider, interne nettsider
og for å åpne større versjon av et bilde.

Variabler:
- src: lenke til bildet
- alt: alternativ tekst
- link: hvor man lander hvis man trykker på bilde.t
- img-caption: tekst som står under bildet

```html
{{< img-caption-link
 figure-class="float"
    class="rounded"
    src="xxxxx"
    alt="xxxxx"
    link="xxxxx"
    img-caption="xxxxx"
  >}}
```

## svkort

Formål: Lager et "kort" på nettsiden til Silicon Valley.

Variabler:
- src: bildefil
- fotograf: navn på fotografen til bildet
- lisenslenke: lenke for å lese mer om lisensen
- lisens: angir hvilken lisens som er brukt
- sourcelenke: lenke til kilden av verket
- source: beskrivelse av hvor verket er hentet fra
- alt: alternativ tekst
- link: hvor man lander hvis man trykker på bilde.t
- header: overskrift på kortet
- adresse: besøksadresse til stedet
- parkering: informasjon om parkering
- betaling: informasjon om inngangspenger
- tid: hvor lang tid det er ment å bruke på stedet
- lenke: lenke til nettside, enten offisiell eller uoffisiell
- kartlenke: lenke til Apple Maps (går automatisk til Google Maps for enheter uten Apple Maps)

```html
{{% svkort
	src="xxxxx"
	fotograf="xxxxx"
	lisenslenke="xxxxx"
	lisens="xxxxx"
	sourcelenke="xxxxx"
	source="xxxxx"
	alt="xxxxx"
	header="xxxxx"
	adresse="xxxxx"
	parkering="xxxxx"
	betaling="xxxxx"
	tid="xxxxx"
	lenke="xxxxx"
	kartlenke="xxxxx"
%}}

xxxxxx

{{% /svkort %}}
```
