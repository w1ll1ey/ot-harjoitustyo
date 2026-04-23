from entities.level import Level
from entities.player import Player
from entities.enemy import Enemy


class GameLogic:
    def __init__(self):
        self.level = Level([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ])
        start_x = 1
        start_y = 1
        damage = 1
        hp = 10
        name = "Remus"
        self.player = Player(start_x, start_y, hp, damage, name)
        self.enemies = []
        self.enemies.append(Enemy(5, 5, hp=3, damage=1, name="Filch"))

    def move_player(self, dx, dy):
        new_x, new_y = self.player.get_new_location(dx, dy)
        wall = self.level.is_wall(new_x, new_y)
        bumped_enemy = False
        
        for enemy in self.enemies:
            if enemy.x == new_x and enemy.y == new_y:
                bumped_enemy = True
                enemy.hp -= self.player.damage
                
                if enemy.hp <= 0:
                    self.enemies.remove(enemy)
                    
                break
        
        if not wall and not bumped_enemy:
            self.player.move(dx, dy)
        
        for enemy in self.enemies:
            enemy_new_x, enemy_new_y, move = enemy.get_new_location(self.player.x, self.player.y)
            
            if enemy_new_x == self.player.x and enemy_new_y == self.player.y:
                self.player.hp = max(0, self.player.hp - enemy.damage)
                
            elif not self.level.is_wall(enemy_new_x, enemy_new_y):
                enemy.move(move)
