from entities.level import Level
from entities.player import Player
from services.game_logic import GameLogic

def main():
    level_matrix = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
    ]
    start_x = 1
    start_y = 1
    HP = 10
    level = Level(level_matrix)
    player = Player(start_x, start_y, HP)
    game = GameLogic(level, player)
    
    game.move_player(1, 1)
    game.move_player(1, 1)
    game.move_player(1, 1)

    
if __name__ == "__main__":
    main()