from services.game_logic import GameLogic
from ui.ui import UI


def main():
    game = GameLogic()
    ui = UI(game)
    ui.start()


if __name__ == "__main__":
    main()
