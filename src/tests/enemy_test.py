import unittest
from entities.enemy import Enemy

class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(5, 5, hp=3, damage=1, name="Test")
        
    def test_new_location_when_enemy_x_is_same_y_is_more(self):
        self.assertEqual(self.enemy.get_new_location(5, 3), (5, 4, (0, -1)))
        
    def test_new_location_when_enemy_x_is_same_y_is_less(self):
        self.assertEqual(self.enemy.get_new_location(5, 7), (5, 6, (0, 1)))
        
    def test_new_location_when_enemy_x_is_more(self):
        self.assertEqual(self.enemy.get_new_location(3, 3), (4, 5, (-1, 0)))
        
    def test_new_location_when_enemy_x_is_less(self):
        self.assertEqual(self.enemy.get_new_location(7, 3), (6, 5, (1, 0)))