class Player:
    """Represents the playable character entity.

    Attributes:
        start_x: Player spawn x coordinate.
        start_y: Player spawn y coordinate.
        hp: Player hitpoints.
        damage: Damage dealt by player attacks.
        name: Name of the player. 
    """

    def __init__(self, start_x, start_y, *, hp, damage, name):
        """Creates the player entity.

        Args:
            start_x: Player spawn x coordinate.
            start_y: Player spawn y coordinate.
            hp: Player hitpoints.
            damage: Damage dealt by player attacks.
            name: Name of the player. 
        """

        self.x = start_x
        self.y = start_y
        self.hp = hp
        self.damage = damage
        self.name = name

    def get_new_location(self, dx, dy):
        """Returns new location of the player based on the move made.

        Args:
            dx: Change of location on x axis.
            dy: Change of location on y axis.

        Returns:
            New location as two integers x, y.
        """

        return self.x + dx, self.y + dy

    def move(self, dx, dy):
        """Changes the location of the player based on the move made.

        Args:
            dx: Change of location on x axis.
            dy: Change of location on y axis.
        """

        self.x += dx
        self.y += dy
