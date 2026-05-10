class Character:
    """Parent class for game entities with position and combat attributes. 
    Manages entity movement on the map.

    Attributes:
        x: Current x coordinate.
        y: Current y coordinate.
        hp: Entity hitpoints.
        damage: Damage dealt by entity attacks.
        name: Name of the entity. 
    """

    def __init__(self, start_x, start_y, *, hp, damage, name):
        """Creates the entity.

        Args:
            start_x: Entity spawn x coordinate.
            start_y: Entity spawn y coordinate.
            hp: Entity hitpoints.
            damage: Damage dealt by entity attacks.
            name: Name of the entity. 
        """

        self.x = start_x
        self.y = start_y
        self.hp = hp
        self.damage = damage
        self.name = name

    def move(self, dxdy):
        """Updates entity position on the map.

        Args:
            dxdy: Tuple (dx, dy) representing change in x and y coordinates.
        """
        self.x += dxdy[0]
        self.y += dxdy[1]
