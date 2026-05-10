from entities.character import Character


class Enemy(Character):
    """Represents non-playable hostile entities.

    Inherits from Character and adds enemy-specific pathfinding logic.

    Inherited Attributes:
        x: Current x coordinate.
        y: Current y coordinate.
        hp: Enemy hitpoints.
        damage: Damage dealt by enemy attacks.
        name: Name of the enemy. 
    """

    def get_new_location(self, player_x, player_y):
        """Returns new location of the enemy based on the current player location.

        Args:
            player_x: Current player x coordinate.
            player_y: Current player y coordinate.

        Returns:
            New location as integers new_x, new_y 
            and move to this location as tuple move (new_x, new_y).
        """

        if self.x == player_x:
            if self.y > player_y:
                new_y = self.y - 1
            else:
                new_y = self.y + 1
            new_x = self.x
        else:
            if self.x > player_x:
                new_x = self.x - 1
            else:
                new_x = self.x + 1
            new_y = self.y
        move = (new_x - self.x, new_y - self.y)
        return new_x, new_y, move
