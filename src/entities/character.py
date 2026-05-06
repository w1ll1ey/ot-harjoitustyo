class Character:
    def __init__(self, start_x, start_y, *, hp, damage, name):
        self.x = start_x
        self.y = start_y
        self.hp = hp
        self.damage = damage
        self.name = name
        
    def move(self, dxdy):
        self.x += dxdy[0]
        self.y += dxdy[1]