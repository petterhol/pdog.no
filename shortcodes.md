# Om denne siden

Her legger jeg inn alle Markdown-malene til shortcodes jeg bruker på nettsiden, slik at jeg lett kan finne dem igjen. Variabler merkes med fem x-sympboler: ```xxxxx``` og vi bruker
[Code and Syntax Highlighting](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code-and-syntax-highlighting)
for å gjerde inn koden.

## Copy

Formål: Legger til en "Kopier"-knapp til hørye for ønsket tekst.

Variabler:
- hiddentext: den faktiske verdien som skal kopieres til utklippstavlen.
- ident: en unik identifiseringsverdi, for Javascript-koden til å vite hvilken verdi som skal kopieres.

```
{{% copy
	hiddentext="xxxxxx"
	ident="xxxxxx"
%}}
xxxxxx {{% /copy %}}
```

## Img-caption-link

Formål: Legger til et klikkbart bilde med bildetekst i grå tekst. Kan både brukes til ekstenre nettsider, interne nettsider
og for å åpne større versjon av et bilde.

Variabler:
- src: lenke til bildet
- alt: alternativ tekst
- link: hvor man lander hvis man trykker på bilde.t
- img-caption: tekst som står under bildet

```
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
- scr: bildefil
- alt: alternativ tekst
- link: hvor man lander hvis man trykker på bilde.t
- header: overskrift på kortet
- adresse: besøksadresse til stedet
- parkering: informasjon om parkering
- tid: hvor lang tid det er ment å bruke på stedet
- lenke: lenke til nettside
- kartlenke: lenke til Apple Maps (går automatisk til Google Maps for enheter uten Apple Maps

```
{{% svkort
	scr="xxxxx"
	alt="xxxxx"
	header="xxxxx"
	adresse="xxxxx"
	parkering="xxxxx"
	tid="xxxxx"
	lenke="xxxxx"
	kartlenke="xxxxx"
%}}

xxxxxx

{{% /svkort %}}
```
