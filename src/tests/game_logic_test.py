import unittest
from services.game_logic import GameLogic
from services.world_state import WorldState
from entities.level import Level
from entities.player import Player
from entities.enemy import Enemy
from data.lore_deck import lore_items
from entities.friendly import Friendly
from data.level_themes import all_themes


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.test_theme = {
        "matrix": [
        [1, 1, 1, 1],
        [2, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
        ],
        "player_spawn": (1, 1),
        "free_tiles": [(2, 1), (1, 2), (2, 2)],
        "min_room_number": 1,
        "enemy_pool": [],
        "lore_pool": [],
        "friendly_pool": []
        }
        test_map = Level(self.test_theme)
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
        
    def test_stepping_on_lore_item_adds_text_to_log(self):
        lore_items["test_lore"] = {
            "text": "This is a test.", 
            "tags": ["read_test_lore"]
        }
        self.game.lore_pool = ["test_lore"]
        self.game.level.matrix = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 3, 0, 1],
            [1, 1, 1, 1]
        ]
        self.game.move_player((0, 1))
        self.assertIn("This is a test.", self.game.log)
        
    def test_stepping_on_lore_item_removes_it(self):
        lore_items["test_lore"] = {
            "text": "This is a test.", 
            "tags": ["read_test_lore"]
        }
        self.game.lore_pool = ["test_lore"]
        self.game.level.matrix = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 3, 0, 1],
            [1, 1, 1, 1]
        ]
        self.game.move_player((0, 1))
        self.assertEqual(self.game.level.matrix[2][1], 0)
        
    def test_stepping_on_lore_item_adds_tag_to_world_state(self):
        lore_items["test_lore"] = {
            "text": "This is a test.", 
            "tags": ["read_test_lore"]
        }
        self.game.lore_pool = ["test_lore"]
        self.game.level.matrix = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 3, 0, 1],
            [1, 1, 1, 1]
        ]
        self.game.move_player((0, 1))
        self.assertIn("read_test_lore", self.game.world_state.tags)
    
    def test_player_cant_move_inside_friendlys(self):
        self.game.friendlys.append(Friendly(2, 1, hp=0, damage=0, name="test", dialogue="helloworld", tags=["seentest"]))
        self.game.move_player((1, 0))
        
        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 1)
        
    def test_friendly_adds_dialogue_to_log_when_bumped(self):
        self.game.friendlys.append(Friendly(2, 1, hp=0, damage=0, name="test", dialogue="helloworld", tags=["seentest"]))
        self.game.move_player((1, 0))
        
        self.assertIn("helloworld", self.game.log)
        
    def test_friendly_adds_tags_to_world_state_when_bumped(self):
        self.game.friendlys.append(Friendly(2, 1, hp=0, damage=0, name="test", dialogue="helloworld", tags=["seentest"]))
        self.game.move_player((1, 0))
        
        self.assertIn("seentest", self.game.world_state.tags)
        
    def test_stepping_on_door_increases_room_number(self):
        all_themes.clear()
        all_themes.append(self.test_theme)
        initial_room = self.game.world_state.room
        self.game.move_player((-1, 0))
        
        self.assertEqual(self.game.world_state.room, initial_room + 1)
        
    def test_stepping_on_door_triggers_teleportation(self):
        all_themes.clear()
        all_themes.append(self.test_theme)
        self.game.move_player((-1, 0))
        
        self.assertEqual(self.game.player.x, 1)
        self.assertEqual(self.game.player.y, 1)
        
    def test_friendly_moves_when_player_moves(self):
        self.game.level.matrix = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.game.friendlys.append(Friendly(5, 3, hp=0, damage=0, name="test", dialogue="helloworld", tags=["seentest"]))
        self.game.move_player((0, 1))
        
        self.assertNotEqual((self.game.friendlys[0].x, self.game.friendlys[0].y), (5, 3))
        
    def test_enemy_moves_when_player_moves(self):
        self.game.level.matrix = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.game.enemies.append(Enemy(5, 3, hp=5, damage=1, name="Enemy"))
        self.game.move_player((0, 1))
        
        self.assertNotEqual((self.game.enemies[0].x, self.game.enemies[0].y), (5, 3))
        