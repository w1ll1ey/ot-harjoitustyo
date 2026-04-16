from entities.level import Level
from entities.player import Player
from entities.enemy import Enemy


class GameLogic:
    def __init__(self, level: Level, player: Player):
        self.level = level
        self.player = player
        self.enemies = []
        self.enemies.append(Enemy(5, 5, 3, "Filch"))

    def move_player(self, dx, dy):
        new_x, new_y = self.player.get_new_location(dx, dy)
        wall = self.level.is_wall(new_x, new_y)

        if not wall:
            self.player.move(dx, dy)
