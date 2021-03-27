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

