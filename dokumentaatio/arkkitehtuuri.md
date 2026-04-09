```mermaid
    classDiagram
        class UI
        class GameLogic
        class Level
        class Player

        UI "1" --> "1" GameLogic
        GameLogic "1" --> "1" Level
        GameLogic "1" --> "1" Player
```
