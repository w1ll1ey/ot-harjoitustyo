import pygame
import os
from services.game_logic import GameLogic


class UI:
    def __init__(self, gamelogic: GameLogic):
        self.game = gamelogic
        self.cell_size = 16
        self.map_width = len(self.game.level.matrix[0]) * self.cell_size
        self.map_height = len(self.game.level.matrix) * self.cell_size
        self.clock = pygame.time.Clock()

        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.map_width + 150, self.map_height))

        current_dir = os.path.dirname(__file__)
        project_root = os.path.join(current_dir, "..")
        ascii_path = os.path.join(project_root, 'assets', 'ascii.png')

        self.sprites = pygame.image.load(ascii_path)
        self.sprites.set_colorkey((255, 0, 255))
        self.textures = {}
        self.textures['#'] = self.sprites.subsurface((32, 32, 16, 16))
        self.textures['.'] = self.sprites.subsurface((208, 32, 16, 16))
        self.textures['@'] = self.sprites.subsurface((240, 48, 16, 16))
        self.textures['F'] = self.sprites.subsurface((80, 64, 16, 16))

        pygame.font.init()
        self.font = pygame.font.SysFont('Courier', 22, bold=True)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.game.move_player(0, -1)
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.game.move_player(-1, 0)
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.game.move_player(0, 1)
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
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

        sidebar_x = self.map_width + 15

        for enemy in self.game.enemies:
            if enemy.name == 'Filch':
                self.screen.blit(
                    self.textures['F'], (enemy.x * self.cell_size, enemy.y * self.cell_size))
                enemy_text = self.font.render("F = Filch", True, (0, 0, 0))
                self.screen.blit(enemy_text, (sidebar_x, 215))

        HP_text = self.font.render(
            f"HP: {self.game.player.hp}/10", True, (0, 0, 0))
        if self.game.player.name == "Remus":
            player_text = self.font.render("@ = Remus", True, (0, 0, 0))
        self.screen.blit(HP_text, (sidebar_x, 5))
        self.screen.blit(player_text, (sidebar_x, 190))
