import unittest
from entities.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(4, 4, 5)
    def test_get_new_location_returns_right_location(self):
        self.assertEqual(self.player.get_new_location(1, 0), (5, 4))
    
    def test_move_changes_coordinates(self):
        self.player.move(1, 0)
        
        self.assertEqual(self.player.x, 5)
        self.assertEqual(self.player.y, 4)