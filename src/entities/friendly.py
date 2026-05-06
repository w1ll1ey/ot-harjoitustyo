import random
from entities.character import Character

class Friendly(Character):
    def __init__(self, start_x, start_y, *, hp, damage, name, dialogue, tags):
        super().__init__(start_x, start_y, hp=hp, damage=damage, name=name)
        self.dialogue = dialogue
        self.tags = tags
        
    def get_new_location(self):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        move = random.choice(moves)
        
        return self.x + move[0], self.y + move[1], move