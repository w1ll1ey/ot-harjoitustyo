import pygame
import os
from services.game_logic import GameLogic


class UI:
    def __init__(self, gamelogic: GameLogic):
        self.game = gamelogic
        self.cell_size = 16
        self.width = len(self.game.level.matrix[0]) * self.cell_size
        self.height = len(self.game.level.matrix) * self.cell_size
        self.clock = pygame.time.Clock()
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        current_dir = os.path.dirname(__file__)
        project_root = os.path.join(current_dir, "..")
        ascii_path = os.path.join(project_root, 'assets', 'ascii.png')
        
        self.sprites = pygame.image.load(ascii_path)
        self.sprites.set_colorkey((255, 0, 255))
        self.textures = {}
        self.textures['#'] = self.sprites.subsurface((32, 32, 16, 16))
        self.textures['.'] = self.sprites.subsurface((208, 32, 16, 16))
        self.textures['@'] = self.sprites.subsurface((240, 48, 16, 16))
        

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.game.move_player(0, -1)
                    elif event.key == pygame.K_a:
                        self.game.move_player(-1, 0)
                    elif event.key == pygame.K_s:
                        self.game.move_player(0, 1)
                    elif event.key == pygame.K_d:
                        self.game.move_player(1, 0)
                        
                    
            self.screen.fill((235, 225, 195))
            self.draw()
            pygame.display.flip()
                
            self.clock.tick(60)
                        
            
    def draw(self):
        for y_index, row in enumerate(self.game.level.matrix):
            for x_index, column in enumerate(row):
                pixel_x = x_index * self.cell_size
                pixel_y = y_index * self.cell_size
                if column == 1:
                    self.screen.blit(self.textures['#'], (pixel_x, pixel_y))
                if column == 0:
                    self.screen.blit(self.textures['.'], (pixel_x, pixel_y))
                    
        player_x = self.game.player.x * self.cell_size
        player_y = self.game.player.y * self.cell_size
        self.screen.blit(self.textures['@'], (player_x, player_y))