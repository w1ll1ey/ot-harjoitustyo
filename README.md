# Ohjelmistotekniikka, harjoitustyö

Sovellus on ruudukkopohjainen, vuoropohjainen luolastoseikkailupeli. Pelaaja ohjaa hahmoa kaksiulotteisessa maailmassa, jossa tavoitteena on tutkia huoneita, välttää/voittaa vihollisia ja kerätä aarteita kerätäkseen pisteitä.

## Dokumentaatio

**Vaatimusmäärittely**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md

**Tuntikirjanptio**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md

**Changelog**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md

## Asennus

1. Asenna riippuvuudet komennolla:

<code>poetry install</code>

2. Käynnistä sovellus komennolla:

<code>poetry run invoke start</code>

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

<code>poetry run invoke start</code>

### Testaus

Testit suoritetaan komennolla:

<code>poetry run invoke test</code>

### Testikattavuus

Testikattavuuden voi generoida komennolla:

<code>poetry run invoke coverage-report</code>

Raportti generoituu htmlcov-kansioon.
