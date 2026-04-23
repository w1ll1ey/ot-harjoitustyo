class Enemy:
    def __init__(self, start_x, start_y, *, hp, damage, name):
        self.x = start_x
        self.y = start_y
        self.hp = hp
        self.damage = damage
        self.name = name
        
    def get_new_location(self, player_x, player_y):
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
    
    def move(self, dxdy):
        self.x += dxdy[0]
        self.y += dxdy[1]