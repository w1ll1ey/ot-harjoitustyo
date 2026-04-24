import unittest
from services.game_logic import GameLogic
from entities.level import Level
from entities.player import Player
from entities.enemy import Enemy


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
        test_map = Level([
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ])
        test_player = Player(1, 1, 5, 1, "Test")

        self.game.level = test_map
        self.game.player = test_player
        self.game.enemies = []

    def test_move_player_valid_move_changes_coordinates(self):
        self.game.move_player(1, 0)

        self.assertEqual(self.game.player.x, 2)
        self.assertEqual(self.game.player.y, 1)

    def test_move_player_into_wall_does_not_change_coordinates(self):
        self.game.move_player(0, -1)

        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 1)

    def test_move_player_into_enemy_drops_hp(self):
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.move_player(1, 0)

        self.assertEqual(self.game.player.hp, 4)

    def test_player_cant_move_inside_enemy(self):
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.move_player(1, 0)

        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 1)

    def test_move_player_ignores_enemy_if_not_bumped(self):
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.move_player(0, 1)

        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 2)
        self.assertEqual(self.game.player.hp, 5)
