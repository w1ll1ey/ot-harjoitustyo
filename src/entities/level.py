class Level:
    def __init__(self, matrix):
        self.matrix = matrix

    def is_wall(self, x, y):
        return self.matrix[y][x] == 1
    
    def is_door(self, x, y):
        return self.matrix[y][x] == 2
