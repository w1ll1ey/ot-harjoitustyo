from entities.level import Level
from entities.player import Player


class GameLogic:
    def __init__(self, level: Level, player: Player):
        self.level = level
        self.player = player

    def move_player(self, dx, dy):
        new_x, new_y = self.player.get_new_location(dx, dy)
        wall = self.level.is_wall(new_x, new_y)

        if wall:
            print("Ouch")

        else:
            self.player.move(dx, dy)
            print(f"Moved to: {self.player.x}, {self.player.y}")
