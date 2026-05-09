import unittest
from unittest.mock import patch
from entities.level import Level


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.test_theme = {
        "matrix": [
        [1, 1, 1, 1],
        [2, 0, 0, 1],
        [1, 3, 0, 1],
        [1, 1, 1, 1]
        ],
        "player_spawn": (1, 1),
        "free_tiles": [(2, 1), (1, 2), (2, 2)]
        }
        self.level = Level(self.test_theme)
    
    def test_is_wall_returns_true_when_wall(self):
        self.assertEqual(self.level.is_wall(0, 0), True)

    def test_is_wall_returns_true_when_out_of_bounds(self):
        self.assertEqual(self.level.is_wall(-1, -1), True)
        
    def test_is_door_returns_true_when_door(self):
        self.assertEqual(self.level.is_door(0, 1), True)
        
    def test_is_door_returns_false_when_out_of_bounds(self):
        self.assertEqual(self.level.is_door(-1, -1), False)
        
    def test_is_lore_returns_true_when_lore(self):
        self.assertEqual(self.level.is_lore(1, 2), True)
        
    def test_is_lore_returns_false_when_out_of_bounds(self):
        self.assertEqual(self.level.is_lore(-1, -1), False)
        
    def test_level_generates_door_on_the_correct_side_with_all_directions(self):
        directions = ["west", "north", "east", "south"]
        
        procedural_theme = {
            "min_width": 4, "max_width": 4,
            "min_height": 4, "max_height": 4,
            "wall_tile": 1, "floor_tile": 0
        }
        
        for direction in directions:
            with patch("entities.level.random.choice") as choice:
                choice.return_value = direction
                level = Level(procedural_theme)
                if direction == "west":
                    left_column = [row[0] for row in level.matrix]
                    self.assertIn(2, left_column)
                    self.assertEqual(level.player_spawn[0], 4)
                elif direction == "north":
                    self.assertIn(2, level.matrix[0])
                    self.assertEqual(level.player_spawn[1], 4)
                elif direction == "east":
                    right_column = [row[5] for row in level.matrix]
                    self.assertIn(2, right_column)
                    self.assertEqual(level.player_spawn[0], 1)
                elif direction == "south":
                    self.assertIn(2, level.matrix[5])
                    self.assertEqual(level.player_spawn[1], 1)