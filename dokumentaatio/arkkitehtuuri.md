# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne noudattaa kolmitasoista kerrosarkkitehtuuria. Koodin pakkausrakenne on seuraava:

```mermaid
graph TD
    ui[ui]
    assets[assets]
    services[services]
    data[data]
    entities[entities]

    ui --> services
    ui --> assets
    services --> entities
    services --> data
```

Pakkaus ui sisältää käyttöliittymästä vastaavan koodin. Pakkaus services sisältää sovelluslogiikasta vastaavan koodin ja entities sisältää tietokohteita edustavat luokat. Data sisältää pelin kovakoodattua dataa sanakirjoihin tallennettuna. Assets sisältää pelin visuaalisen esittämisen vaatimat mediatiedostot.

## Käyttöliittymä

Käyttöliittymä on eriytetty täysin sovelluslogiikasta. Siitä vastaa UI-luokka, joka hyödyntää Pygame-kirjastoa.

Käyttöliittymä vastaa:

    - Näppäimistösyötteiden lukemisesta

    - Pelitilan (kartta, hahmot, lokitekstit) piirtämisestä ruudulle

Käyttöliittymä ei itse muokkaa pelin tilaa, vaan kutsuu ainoastaan sovelluslogiikan (GameLogic) metodeja, kuten move_player(). Kun sovelluslogiikka on päivittänyt tilan, UI kutsuu omaa draw()-metodiaan renderöidäkseen uuden tilanteen ruudulle.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat Character, Player, Enemy, Friendly ja Level.

WorldState-luokka ylläpitää maailman tietoja ja syöttää niitä GameLogic-luokalle, jotta tämä tietää miten toimia.

Varsinaisesta sovelluslogiikasta vastaa GameLogic-luokka, joka tarjoaa käyttöliittymälle metodit pelin tilan muokkaamiseen.

GameLogic käyttää näiden toiminnallisuuksien toteuttamiseen entities-pakkauksen luokkia ja data-pakkauksen tietoja. Se tarkistaa siirtojen laillisuuden ja päivittää niiden pohjalta pelitilaa.

Ohjelman osien väliset suhteet selviävät seuraavasta luokka-/pakkauskaaviosta:

```mermaid
    classDiagram
    namespace ui {
        class UI
    }

    namespace services {
        class GameLogic
        class WorldState
    }

    namespace entities {
        class Character
        class Player
        class Enemy
        class Friendly
        class Level
    }

    namespace assets {
        class ascii_png {
            <<file>>
        }
    }

    namespace data {
        class hostile_mobs {
            <<module>>
        }
        class level_themes {
            <<module>>
        }
        class lore_deck {
            <<module>>
        }
    }

    UI "1" --> "1" GameLogic
    UI ..> ascii_png
    GameLogic "1" --> "1" WorldState
    GameLogic "1" --> "1" Level
    GameLogic "1" --> "1" Player
    Player --|> Character
    GameLogic "1" --> "*" Enemy
    Enemy --|> Character
    GameLogic "1" --> "*" Friendly
    Friendly --|> Character
    GameLogic ..> hostile_mobs
    GameLogic ..> level_themes
    GameLogic ..> lore_deck
```

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikkaa sekvenssikaavioiden avulla. Seuraavat kaksi sekvenssikaaviota edustavat esimerkkejä siitä, miten pelilogiikka hallinoi maailman päivittämistä eri tilanteissa.

### Pelaajan liikkuminen tyhjään ruutuun

Kun pelaaja valitsee liikkua kartalla alaspäin ruutuun, joka on tyhjä lattiaruutu ilman lähettyvillä olevia vihollisia, maailma päivittyy seuraavasti:

```mermaid
    sequenceDiagram
        actor User
        User->>UI: Presses 'S'
        UI->>GameLogic: move_player(0, 1)
        GameLogic->>Player: get_new_location(0, 1)
        Player-->>GameLogic: 1, 2
        GameLogic->>Level: is_wall(1, 2)
        Level-->>GameLogic: False
        GameLogic->>Level: is_door(1, 2)
        Level-->>GameLogic: False
        GameLogic->>Level: is_lore(1, 2)
        Level-->>GameLogic: False
        loop every friendly in self.friendlys
            Note over GameLogic: list empty
        end
        loop every enemy in self.enemies
            GameLogic->>Enemy: x, y
            Enemy-->>GameLogic: 2, 1

            opt x != new_x or y != new_y
                Note over GameLogic, Enemy: no collision
            end
        end
        GameLogic->>GameLogic: bumped_enemy
        GameLogic-->>GameLogic: False
        opt is_wall == False and bumped_enemy == False
            GameLogic->>Player: move(0, 1)
            Player-->>GameLogic: return
            opt is_door != True
                Note over GameLogic, Level: no collision
            end
            opt is_lore != True
                Note over GameLogic, Level: no collision
            end
        end
        loop every enemy in self.enemies
            GameLogic->>Enemy: get_new_location(1, 2)
            Enemy-->>GameLogic: 1, 1, (-1, 0)
            opt enemy_new_x != player.x or enemy_new_y != player.y
                GameLogic->>Level: is_wall(1, 1)
                Level-->>GameLogic: False
            end
            opt is_wall == False
                GameLogic->>Enemy: move(-1, 0)
                Enemy-->>GameLogic: return
            end
        end
        GameLogic-->>UI: return
        UI->>UI: draw()
```

Metodi move_player löytää ensin pelaajan uuden hypoteettisen lokaation. Se tarkastaa ennen liikkumista, törmääkö pelaaja NPC:n tai seinään ja todettuaan että näin ei ole, liikuttaa pelaajaa. Seuraavaksi se tarkastaa kävelikö pelaaja oven tai esineen päälle, ja todettuaan että näinkään ei ole, jatkaa eteenpäin. Metodi hakee vihollisten uudet hypoteettiset lokaatiot ja tarkistaa ennen liikkumista, törmäävätkö nämä pelaajaan tai seiniin. Todettuaan että näin ei ole, se liikuttaa näitä. Lopuksi UI-luokka piirtää päivittyneen tilanteen.

### Pelaajan liikkuminen vihollisen ruutuun

Kun pelaaja valitsee liikkua kartalla oikealle ruutuun, jossa on parhaillaan vihollinen, maailma päivittyy seuraavasti:

```mermaid
    sequenceDiagram
        actor User
        User->>UI: Presses "D"
        UI->>GameLogic: move_player(1, 0)
        GameLogic->>Player: get_new_location(1, 0)
        Player-->>GameLogic: 2, 1
        GameLogic->>Level: is_wall(2, 1)
        Level-->>GameLogic: False
        GameLogic->>Level: is_door(2, 1)
        Level-->>GameLogic: False
        GameLogic->>Level: is_lore(2, 1)
        Level-->>GameLogic: False
        loop every friendly in self.friendlys
            Note over GameLogic: list empty
        end
        loop every enemy in self.enemies
            GameLogic->>Enemy: x, y
            Enemy-->>GameLogic: 2, 1
            opt x == new_x and y == new_y
                GameLogic->>Enemy: hp -= player.damage
                Enemy-->>GameLogic: return
                GameLogic->>Enemy: hp
                Enemy-->>GameLogic: 2
                opt enemy.hp > 0
                    Note over GameLogic, Enemy: enemy stays on the map
                end
            end
        end
        GameLogic->>GameLogic: bumped_enemy
        GameLogic-->>GameLogic: True
        opt is_wall != False or bumped_enemy != False
            Note over GameLogic, Level: player won't move
        end
        loop every enemy in self.enemies
            GameLogic->>Enemy: get_new_location(1, 1)
            Enemy-->>GameLogic: 1, 1, (-1, 0)

            opt enemy_new_x == player.x and enemy_new_y == player.y
                GameLogic->>Player: hp = max(0, hp - enemy.damage)
                Player-->>GameLogic: return
            end
        end
        GameLogic->>Player: hp
        Player-->>GameLogic: 9
            opt player.hp > 0
                Note over GameLogic, Player: game continues
            end
        GameLogic-->>UI: return
        UI->>UI: draw()
```

Metodi move_player löytää ensin pelaajan uuden hypoteettisen lokaation. Se tarkastaa ennen liikkumista, törmääkö pelaaja NPC:n tai seinään ja todettuaan että pelaaja törmää viholliseen, se vähentää viholliselta HP:ta ja tarkastaa kuoleeko vihollinen. Pelaaja ei tällöin liiku. Metodi hakee vihollisten uudet hypoteettiset lokaatiot ja tarkistaa ennen liikkumista, törmäävätkö nämä pelaajaan tai seiniin. Todettuaan että vihollinen törmää pelaajaan, se vähentää pelaajalta HP:ta ja tarkastaa kuoleeko pelaaja. Vihollinen ei tällöin liiku. Lopuksi UI-luokka piirtää päivittyneen tilanteen.

### Muut toiminnallisuudet

Peli noudattaa pitkälti samaa looppia kaikilla muillakin syötteillä. Käyttöliittymä lukee syötteen ja antaa sen käsiteltäväksi pelilogiikalle, joka kiertää saman kaavan läpi eri haarautumilla riippuen siitä, mihin pelaaja liikkuu. Pelimaailma päivittyy ja käyttöliittymä tulostaa päivittyneen maailman käyttäjän näytölle.

## Ohjelmaan jääneet heikkoudet

### Pysyväistallennus

Vastoin kurssin suosituksia pelissä ei ole minkäänlaista pysyväistallennusta. Pelin luonteen vuoksi koin sen olevan jokseenkin triviaali ominaisuus tämän hetkiselle toteutukselle. Jos yksittäinen pelikerta pitenee, mahdollisuus tallentaa kesken yrityksen on luonnollisesti tarpeellista. Tallenus voitaisiin toteuttaa esim. tallentamalla JSON-tiedostoon WorldState, pelaajan sijainti/HP, huoneen matriisi sekä aktiiviset NPC:t.

### Tarinan yksinkertaisuus

Suhteessa pelimoottorin luomiin mahdollisuuksiin koen, että pelattavissa oleva demo antaa pelistä jokseenkin yksinkertaisen kuvan. Minua inspiroi erityisesti idea modulaarisesta pelimoottorista, joten halusin keskittyä sen luomiseen, mikä johti siihen että en ehkä onnistunut hyödyntämään sitä täydellisesti demossa. Positiivisena puolena tarina on jatkossa helposti skaalattavissa.
