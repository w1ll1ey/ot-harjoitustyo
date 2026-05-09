import unittest
from services.game_logic import GameLogic
from services.world_state import WorldState
from entities.level import Level
from entities.player import Player
from entities.enemy import Enemy


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        test_theme = {
        "matrix": [
        [1, 1, 1, 1],
        [2, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
        ],
        "player_spawn": (1, 1),
        "free_tiles": [(2, 1), (1, 2), (2, 2)]
        }
        test_map = Level(test_theme)
        test_player = Player(1, 1, hp=5, damage=1, name="Test")
        test_state = WorldState()
        self.game = GameLogic(world_state=test_state, level=test_map, player=test_player)

    def test_move_player_valid_move_changes_coordinates(self):
        self.game.move_player((1, 0))

        self.assertEqual(self.game.player.x, 2)
        self.assertEqual(self.game.player.y, 1)

    def test_move_player_into_wall_does_not_change_coordinates(self):
        self.game.move_player((0, -1))

        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 1)

    def test_move_player_into_enemy_drops_hp(self):
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.move_player((1, 0))

        self.assertEqual(self.game.player.hp, 4)

    def test_player_cant_move_inside_enemy(self):
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.move_player((1, 0))

        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 1)

    def test_move_player_ignores_enemy_if_not_bumped(self):
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.move_player((0, 1))

        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 2)
        self.assertEqual(self.game.player.hp, 5)

    def test_enemy_gets_removed_when_dead(self):
        self.game.enemies.append(Enemy(2, 1, hp=1, damage=1, name="Enemy"))
        self.game.move_player((1, 0))

        self.assertEqual(self.game.enemies, [])

    def test_enemy_coordinates_dont_change_if_move_would_hit_wall(self):
        self.game.level.matrix = [
            [1, 1, 1, 1],
            [2, 0, 0, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1]
        ]
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.player = Player(2, 3, hp=5, damage=1, name="Test")
        self.game.move_player((0, -1))

        self.assertEqual(self.game.enemies[0].x, 2)
        self.assertEqual(self.game.enemies[0].y, 1)

    def test_dying_activates_game_over(self):
        self.game.player = Player(1, 1, hp=1, damage=1, name="Test")
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.move_player((0, -1))

        self.assertEqual(self.game.world_state.game_over, True)

    def test_dying_activates_game_over_message(self):
        self.game.player = Player(1, 1, hp=1, damage=1, name="Test")
        self.game.enemies.append(Enemy(2, 1, hp=5, damage=1, name="Enemy"))
        self.game.move_player((0, -1))

        self.assertIn("GAME OVER! Press Enter to restart.", self.game.log)

    def test_game_log_doesnt_get_too_long(self):
        self.game.log = ["1", "2", "3", "4", "5", "6"]
        self.game.add_message("7")

        self.assertEqual(len(self.game.log), 6)
