from entities.character import Character


class Player(Character):
    """Represents the playable character entity.

    Inherits from Character and adds player-specific location-finding logic.

    Inherited Attributes:
        x: Current x coordinate.
        y: Current y coordinate.
        hp: Player hitpoints.
        damage: Damage dealt by player attacks.
        name: Name of the player. 
    """

    def get_new_location(self, dxdy):
        """Returns new location of the player based on the move made.

        Args:
            dx: Change of location on x axis.
            dy: Change of location on y axis.

        Returns:
            New location as two integers x, y.
        """

        return self.x + dxdy[0], self.y + dxdy[1]
