from services.world_state import WorldState
from services.game_logic import GameLogic
from ui.ui import UI


def main():
    world_state = WorldState()
    game = GameLogic(world_state)
    ui = UI(game)
    ui.start()


if __name__ == "__main__":
    main()
