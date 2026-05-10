import random
from entities.character import Character

class Friendly(Character):
    """Represents non-playable friendly entities.
    
    Inherits from Character and adds friendly-specific move logic and attributes.

    Inherited Attributes:
        x: Current x coordinate.
        y: Current y coordinate.
        hp: Friendly hitpoints.
        damage: Damage dealt by friendly attacks.
        name: Name of the friendly. 
        
    Attributs:
        dialogue: Dialogue assigned for the friendly.
        tags: Tags held by the friendly. 
    """
    
    def __init__(self, start_x, start_y, *, hp, damage, name, dialogue, tags):
        """Creates the friendly entity.

        Args:
            start_x: Friendly spawn x coordinate.
            start_y: Friendly spawn y coordinate.
            hp: Friendly hitpoints.
            damage: Damage dealt by friendly attacks.
            name: Name of the friendly.
            dialogue: Dialogue assigned for the friendly.
            tags: Tags held by the friendly. 
        """
        
        super().__init__(start_x, start_y, hp=hp, damage=damage, name=name)
        self.dialogue = dialogue
        self.tags = tags
        
    def get_new_location(self):
        """Returns new location of the friendly based on the chosen random move.

        Returns:
            New location as integers 
            and move to this location as tuple move.
        """
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        move = random.choice(moves)
        
        return self.x + move[0], self.y + move[1], move