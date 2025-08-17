# pdog.no

Hjemmeside for Petter Holstad. <https://pdog.no>

## Forutsetninger

Installer [Hugo](https://gohugo.io/getting-started/installing/).

## Bygg nettsiden

For å bygge nettsiden må du være i prosjektmappen og kjøre `hugo`.

```shell
cd pdog.no
hugo
```

Denne kommandoen genererer alle filene som hører til nettsiden i en mappe ved
navn `public`. Innholdet i `public` kan nå kopieres til webhotellet.

## Markdownlint

Vi bruker markdownlint-verktøyet i dette prosjektet. Enhver merge må gjennom en
markdownlint-kontroll. For å unngå for mange markdownlint-commits, bruker vi
[https://dlaa.me/markdownlint/](https://dlaa.me/markdownlint/) til å kontrollere
dokumentene før vi commiter.

## hugo validator

Det er også installert en kontroll for hugo som sjekker de ferdige HTML-filene
som genereres. For å unngå for mange hugo-commits, bruker vi
[https://html5.validator.nu](https://html5.validator.nu) til å kontrollere dokumentene
før vi commiter.

*Hugo validator er foreløpig deaktivert grunnet en uløselig konflikt i pull
request #44. Denne aktiveres på et senere tidspunkt*.
