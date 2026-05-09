import unittest
from services.world_state import WorldState

class TestWorldState(unittest.TestCase):
    def setUp(self):
        self.world_state = WorldState()
        
    def test_add_tags_expands_the_list(self):
        self.world_state.add_tags(["test1", "test2"])

        self.assertEqual(len(self.world_state.tags), 2)
        
    def test_add_tags_gets_won_string_triggers_win_condition(self):
        self.world_state.add_tags(["won"])
        
        self.assertEqual(self.world_state.game_won, True)
        
    def test_meets_prerequisites_success(self):
        self.world_state.tags.add("test")
        
        self.assertEqual(self.world_state.meets_prerequisites(["test"]), True)
        
    def test_meets_prerequisites_failure(self):
        self.assertEqual(self.world_state.meets_prerequisites(["test"]), False)
        
    def test_meets_requirements_success_when_no_prerequisites(self):
        self.assertEqual(self.world_state.meets_prerequisites([]), True)