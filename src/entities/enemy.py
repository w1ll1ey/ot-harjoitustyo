class Enemy:
    def __init__(self, start_x, start_y, hp, damage, name):
        self.x = start_x
        self.y = start_y
        self.hp = hp
        self.damage = damage
        self.name = name