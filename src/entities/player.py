class Player:
    def __init__(self, start_x, start_y, hp):
        self.x = start_x
        self.y = start_y
        self.hp = hp

    def get_new_location(self, dx, dy):
        return self.x + dx, self.y + dy

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
