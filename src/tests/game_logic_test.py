import unittest
from services.game_logic import GameLogic
from entities.level import Level
from entities.player import Player


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        level = Level([
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ])
        player = Player(1, 1, 5)
        self.game = GameLogic(level, player)

    def test_move_player_valid_move_changes_coordinates(self):
        self.game.move_player(1, 0)

        self.assertEqual(self.game.player.x, 2)
        self.assertEqual(self.game.player.y, 1)

    def test_move_player_into_wall_does_not_change_coordinates(self):
        self.game.move_player(0, 1)

        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 1)
