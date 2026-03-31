import pygame
from services.game_logic import GameLogic

class UI:
    def __init__(self, gamelogic: GameLogic):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        
        self.game = gamelogic
        self.cell_size = 50
    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill((0, 0, 0))
            
            pygame.display.flip()
        