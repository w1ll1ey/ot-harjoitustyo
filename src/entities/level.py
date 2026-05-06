import random

class Level:
    """Represents the level entity.

    Attributes:
        matrix: Map of the level.
    """

    def __init__(self, theme):
        """Creates the level entity.

        Args:
            matrix: Map of the level.
        """

        width = random.randint(theme["min_width"], theme["max_width"])
        height = random.randint(theme["min_height"], theme["max_height"])
        self.matrix = [[theme["wall_tile"] for x in range (width + 2)] for y in range (height + 2)]
        start_x = 1
        start_y = 1

        north_door = (random.randint(start_x + 1, start_x + width - 2), start_y - 1)
        south_door = (random.randint(start_x + 1, start_x + width - 2), start_y + height)
        west_door = (start_x - 1, random.randint(start_y + 1, start_y + height - 2))
        east_door = (start_x + width, random.randint(start_y + 1, start_y + height - 2))
        door_direction = random.choice(["north", "south", "west", "east"])
        if door_direction == "north":
            self.matrix[north_door[1]][north_door[0]] = 2
            self.player_spawn = (random.randint(start_x + 1, start_x + width - 2), start_y + height - 1)
        elif door_direction == "south":
            self.matrix[south_door[1]][south_door[0]] = 2
            self.player_spawn = (random.randint(start_x + 1, start_x + width - 2), start_y)
        elif door_direction == "west":
            self.matrix[west_door[1]][west_door[0]] = 2
            self.player_spawn = (start_x + width - 1, random.randint(start_y + 1, start_y + height - 2),)
        else:
            self.matrix[east_door[1]][east_door[0]] = 2
            self.player_spawn = (start_x, random.randint(start_y + 1, start_y + height - 2),)
            
        self.free_tiles = []
        for y in range(start_y, start_y + height):
            for x in range(start_x, start_x + width):
                self.matrix[y][x] = theme["floor_tile"]
                if (x, y) != self.player_spawn:
                    self.free_tiles.append((x, y))
    
    def in_bounds(self, x, y):
        return 0 <= y < len(self.matrix) and 0 <= x < len(self.matrix[0])
                    
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
    
    def is_lore(self, x, y):
        if not self.in_bounds(x, y):
            return False
        return self.matrix[y][x] == 3
