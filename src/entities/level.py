class Level:
    def __init__(self, map):
        self.map = map
        
    def is_wall(self, x, y):
        return self.map[y][x] == 1