# Marauder's Map

Sovellus on ruudukkopohjainen, vuoropohjainen luolastoseikkailupeli. Pelaaja ohjaa hahmoa satunnaisgeneraatioon pohjautuvassa kaksiulotteisessa maailmassa, jossa tavoitteena on etsiä tarvittavat esineet huoneista vältellen vihollisia tai taistellen niitä vastaan. Teema ammentaa All the Young Dudes-kirjasta. Pelimoottori on rakennettu modulaarista valmiutta ajatellen, eli sillä voi halutessaan luoda monenlaisia haarautuvia tarinoita. Pelattavissa oleva versio on melko lineearinen esimerkkitarina, joskin kahta samanlaista pelikertaa ei siinäkään ole. Pelin voittaa löytämällä kaikki tarvittavat esineet ja palaamalla aloitushuoneeseen. Pelin häviää osumapisteiden (HP) pudotessa nollaan.

## Dokumentaatio

**Vaatimusmäärittely**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md

**Tuntikirjanpito**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md

**Changelog**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md

**Arkkitehtuuri**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md

**Käyttöohje**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md

**Testausdokumentti**: https://github.com/w1ll1ey/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md

**Release 1**: https://github.com/w1ll1ey/ot-harjoitustyo/releases/tag/viikko5

**Release 2**: https://github.com/w1ll1ey/ot-harjoitustyo/releases/tag/viikko6

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

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi tehdä komennolla:

<code>poetry run invoke lint</code>
