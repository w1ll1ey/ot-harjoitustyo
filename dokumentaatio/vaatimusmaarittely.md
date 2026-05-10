# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on ruudukkopohjainen, vuoropohjainen luolastoseikkailupeli. Pelaaja ohjaa hahmoa satunnaisgeneraatioon pohjautuvassa kaksiulotteisessa maailmassa, jossa tavoitteena on etsiä tarvittavat esineet huoneista vältellen vihollisia tai taistellen niitä vastaan. Teema ammentaa All the Young Dudes-kirjasta. Pelimoottori on rakennettu modulaarista valmiutta ajatellen, eli sillä voi halutessaan luoda monenlaisia haarautuvia tarinoita. Pelattavissa oleva versio on melko lineearinen esimerkkitarina, joskin kahta samanlaista pelikertaa ei siinäkään ole. Pelin voittaa löytämällä kaikki tarvittavat esineet ja palaamalla aloitushuoneeseen. Pelin häviää osumapisteiden (HP) pudotessa nollaan.

## Käyttäjät

Sovelluksessa on vain yksi käyttäjärooli eli pelaaja.

## Perusversion tarjoama toiminnallisuus

### Pelikenttä ja maailma

- Pelikenttä koostuu ruudukosta, jossa on seiniä sekä kulkukelpoista lattiaa. _TEHTY_
- Pelikenttä voidaan ladata sovelluksen käynnistyessä valmiista matriisista. _TEHTY_

### Pelaajan hallinta

- Pelaaja voi liikkua neljään pääilmansuuntaan (WASD). _TEHTY_
- Pelaaja ei voi liikkua seinien tai NPC:den läpi. _TEHTY_

### Pelimekaniikka

- Peli on vuoropohjainen, pelimaailma päivittyy vain pelaajan liikkuessa. _TEHTY_
- Pelaajalla on osumapisteet (HP) jotka näytetään käyttöliittymässä. _TEHTY_

### Käyttöliittymä

- Graafinen esitys luolastosta (esim. ASCII-merkistö) _TEHTY_

## Jatkokehitysideoita

- Pelistä löytyy erilaisia vihollisia _TEHTY_
- Pelissä on message log _TEHTY_
- Pelissä on kerättäviä objekteja _TEHTY_
- Luolasto generoituu satunnaisesti _TEHTY_
- Mahdollisuus siirtyä uusiin huoneisiin ovien kautta _TEHTY_
- Pelissä on maailmantila, jonka avulla tarinasta voi luoda haarautuvan _TEHTY_
- Pelissä on ystävällisiä NPC:itä _TEHTY_
- Pelissä on dialogia _TEHTY_
