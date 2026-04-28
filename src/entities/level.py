class Level:
    """Represents the level entity.

    Attributes:
        matrix: Map of the level.
    """

    def __init__(self, matrix):
        """Creates the level entity.

        Args:
            matrix: Map of the level.
        """

        self.matrix = matrix

    def is_wall(self, x, y):
        """Checks if the given coordinate represents a wall on the map.

        Args:
            x: The x coordinate.
            y: The y coordinate.

        Returns:
            True if the given coordinate is a wall tile, False if it isn't.
        """

        return self.matrix[y][x] == 1

    def is_door(self, x, y):
        """Checks if the given coordinate represents a door on the map.

        Args:
            x: The x coordinate.
            y: The y coordinate.

        Returns:
            True if the given coordinate is a door tile, False if it isn't.
        """

        return self.matrix[y][x] == 2
