# ryddedagen.no

Hjemmeside for ryddedagen.no.

## Forutsetninger

Installer [Hugo](https://gohugo.io/getting-started/installing/).

## Bygg nettsiden

For å bygge nettsiden må du være i prosjektmappen og kjøre `hugo`.

```shell
cd ryddedagen.no
hugo
```

Denne kommandoen genererer alle filene som hører til nettsiden i en mappe ved
navn `public`. Innholdet i `public` kan nå kopieres til webhotellet.

## Markdownlint

Vi bruker markdownlint-verktøyet i dette prosjektet. Enhver merge må gjennom en
markdownlint-kontroll. For å unngå for mange markdownlint-commits, bruker vi
[https://dlaa.me/markdownlint/](https://dlaa.me/markdownlint/) til å kontrollere
dokumentene før vi commiter.

## HTML5-validering

Hver merge går gjennom en HTML5-validering. `hugo`-jobben i
`.github/workflows/main.yml` bygger nettsiden med `hugo --minify` og kjører
[v.Nu](https://validator.github.io/validator/) mot alt som havner i `public/`.
Valideringen kjøres to ganger: først med `--show-warnings`, som bare er til
informasjon, og så uten, og det er den siste som feller bygget hvis den finner
feil.

For å slippe unødvendige rettecommits kan du kontrollere en side før du
commiter, enten på [html5.validator.nu](https://html5.validator.nu) eller
lokalt:

```shell
pip install html5validator
hugo --minify
html5validator --root public/ --show-warnings
```

Merk at `html5validator` trenger Java installert.
