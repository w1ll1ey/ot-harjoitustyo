# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

## Ohjelman käynnistäminen

1. Asenna riippuvuudet komennolla:

<code>poetry install</code>

2. Käynnistä sovellus komennolla:

<code>poetry run invoke start</code>

## Pelin tavoite

Olet Remus Lupin. Tavoitteenasi on etsiä tarvittavat tavarat Tylypahkan huoneista jotta voitte pitää hauskaa ystäväsi Sirius Mustan kanssa. On kuitenkin jo ilta, eikä tupien ulkopuolelle saisi mennä! Varo siis huoneissa liikkuvia hahmoja, jotka eivät kaihda väkivaltaa sängyistä poistuneita oppilaita kohtaan.

## Kontrollit

Peliä pelataan näppäimistöllä. Peli on vuoropohjainen: aina kun teet siirron, muut hahmot tekevät oman siirtonsa.

    - W tai Nuoli ylös: Liiku ylös

    - S tai Nuoli alas: Liiku alas

    - A tai Nuoli vasemmalle: Liiku vasemmalle

    - D tai Nuoli oikealle: Liiku oikealle

    - Enter: Aloita peli alusta (kuoleman tai voiton jälkeen)

## Pelinäkymä ja karttamerkit

Ruutu on jaettu kahteen osaan: vasemmalla on varsinainen pelikartta ja oikealla infopaneeli.

### Karttamerkit

Liikut kartalla, joka koostuu erilaisista ASCII-merkeistä:

    @ : Remus (Pelaaja)

    Eri kirjaimet : NPC:t (selitetty legendissä)

    + : Ovi

    ? : Esine

    # : Seinä

    . : Lattia

### Infopaneeli

    HP: Näyttää Remuksen nykyiset osumapisteet (esim. 10/10). Jos joudut taisteluun vihollisen kanssa ja HP tippuu nollaan, peli päättyy.

    Loki: Näyttää reaaliaikaisesti viimeisimmät tapahtumat.

    Map legend: Näyttää selitykset kartan merkeistä.
