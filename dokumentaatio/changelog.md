## Viikko 2

- Suunniteltu ja ideoitu sovelluksen tarkoitusta ja rakennetta
- Kirjoitettu sovelluksen vaatimusmäärittely

## Viikko 3

- Sovelluksen toiminnallinen pohja luotu
- Luotu luokat Level ja Player, jotka vastaavat näiden entiteettien käytöksestä
- Luotu GameLogic-luokka, joka vastaa pelin logiikan toiminnasta
- Luotu UI-luokka joka vastaa graafisen käyttöliittymän toiminnasta, toistaiseksi graafinen käyttöliittymä on vain musta ruutu
- Testattu, että Level-luokka tunnistaa missä huoneen seinät ovat

## Viikko 4

- Laajennettu UI-luokan toiminnallisuutta niin, että se luo kartan ja pelaajan jota voi liikutella kartalla
- Luotu testit Player- ja GameLogic-luokille

## Viikko 5

- Luotu uusi Enemy-luokka, joka vastaa vihollisten käytöksestä
- Refaktoroitu pelilogiikan koodia ja lisätty siihen sekä UI-luokkaan vihollisen syntyminen
- Laajennettu UI-luokan toiminnallisuutta näyttämään alkeellinen legend kartan oikealla puolella
- Laajennettu testaus Enemy-entiteetteihin

## Viikko 6

- Luotu taistelumekaniikka, vihollisen tekoäly sekä tapahtumaloki
- Luotu mahdollisuus pelin häviämiselle ja voittamiselle
- Laajennettu UI-luokkaa näyttämään tapahtumalokia
- Laajennettu testaus kattamaan uudet ominaisuudet

## Loppupalautus

- Lisätty WorldState-luokka, joka ylläpitää huoneiden välistä etenemistä ja proseduraalista tarinalogiikkaa
- Toteutettu huoneiden satunnaisgenerointi eri teemoilla sekä niiden sisällön sijoittelu lore- ja vihollislistojen perusteella
- Lisätty lore-esineet, dialogipuu ja ystävähahmot, joiden avulla peliin tuli etenemistä ohjaava tarinallinen puoli
- Toteutettu ystävähahmon satunnainen liikkuminen huoneessa ja vuorovaikutus dialogin kautta
- Laajennettu käyttöliittymää tukemaan isoja huoneita pelaajaa seuraavalla kameralla
- Laajennettu testaus uusiin ominaisuuksiin, poislukien GameLogicissa tapahtuva proseduraalisen tarinankerronnan hallintaan liittyviä ominaisuuksia
