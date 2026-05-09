import unittest
from entities.level import Level


class TestLevel(unittest.TestCase):
    def test_is_wall_returns_true_when_wall(self):
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
        level = Level(test_theme)

        self.assertEqual(level.is_wall(0, 0), True)
