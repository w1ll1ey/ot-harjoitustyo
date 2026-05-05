import pygame
import os
from services.game_logic import GameLogic


class UI:
    """Handles the user interface of the game.

    Attributes:
        game: The current game session.
        cell_size: Size of one game tile in pixels.
        map_width: Width of the visible map in pixels.
        map_height: Height of the visible map in pixels.
        sidebar_width: Width of the sidebar in pixels.
        clock: Init for the game clock.
        screen: Init pygame display window.
        sprites: Ascii tileset for the textures.
        textures: Dictionary containing textures for specific tiles.
        font: General font for the user interface.
        font_log: Font used in printing the event messages.
    """

    def __init__(self, gamelogic: GameLogic):
        """Initializes the pygame session.

        Args:
            gamelogic: The current game session.
        """

        self.game = gamelogic
        self.viewport_tiles_x = 20
        self.viewport_tiles_y = 15
        self.cell_size = 16
        self.viewport_width = self.viewport_tiles_x * self.cell_size
        self.viewport_height = self.viewport_tiles_y * self.cell_size
        self.sidebar_width = 500
        self.clock = pygame.time.Clock()

        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.viewport_width + self.sidebar_width, self.viewport_height))

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
        self.textures['S'] = self.sprites.subsurface((32, 80, 16, 16))
        self.textures['R'] = self.sprites.subsurface((16, 80, 16, 16))
        self.textures['+'] = self.sprites.subsurface((160, 32, 16, 16))
        self.textures['?'] = self.sprites.subsurface((224, 48, 16, 16))

        pygame.font.init()
        self.font = pygame.font.SysFont('Courier', 22, bold=True)
        self.log_font = pygame.font.SysFont('Courier', 18, bold=True)

    def start(self):
        """Launches the pygame session and handles user inputs.
        """

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if self.game.game_over:
                        if event.key == pygame.K_RETURN:
                            self.game = GameLogic()
                        continue
                    elif self.game.game_won:
                        if event.key == pygame.K_RETURN:
                            self.game = GameLogic()
                        continue
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
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
        """Renders currently visible textures to the screen.
        """

        room_width = len(self.game.level.matrix[0])
        room_height = len(self.game.level.matrix)
        if room_width < self.viewport_tiles_x:
            camera_x = (room_width - self.viewport_tiles_x) // 2
        else:
            camera_x = self.game.player.x - (self.viewport_tiles_x // 2)
            max_x = room_width - self.viewport_tiles_x
            camera_x = max(0, min(camera_x, max_x))
        if room_height < self.viewport_tiles_y:
            camera_y = (room_height - self.viewport_tiles_y) // 2
        else:
            camera_y = self.game.player.y - (self.viewport_tiles_y // 2)
            max_y = room_height - self.viewport_tiles_y
            camera_y = max(0, min(camera_y, max_y))
        
        for screen_y in range(self.viewport_tiles_y):
            for screen_x in range(self.viewport_tiles_x):
                tile_x = camera_x + screen_x
                tile_y = camera_y + screen_y
                if not self.game.level.in_bounds(tile_x, tile_y):
                    continue
                tile = self.game.level.matrix[tile_y][tile_x]
                
                pixel_x = screen_x * self.cell_size
                pixel_y = screen_y * self.cell_size
                
                if tile == 1:
                    self.screen.blit(self.textures['#'], (pixel_x, pixel_y))
                if tile == 0:
                    self.screen.blit(self.textures['.'], (pixel_x, pixel_y))
                if tile == 2:
                    self.screen.blit(self.textures['+'], (pixel_x, pixel_y))
                if tile == 3:
                    self.screen.blit(self.textures['?'], (pixel_x, pixel_y))

        player_x = (self.game.player.x - camera_x) * self.cell_size
        player_y = (self.game.player.y - camera_y) * self.cell_size
        self.screen.blit(self.textures['@'], (player_x, player_y))

        sidebar_x = self.viewport_width + 15
        current_legend_y = 215
        drawn_names = []

        for enemy in self.game.enemies:
            enemy_x = enemy.x - camera_x
            enemy_y = enemy.y - camera_y
            enemy_pixel_x = enemy_x * self.cell_size
            enemy_pixel_y = enemy_y * self.cell_size
            if enemy_x < 0 or enemy_x >= self.viewport_tiles_x or enemy_y < 0 or enemy_y >= self.viewport_tiles_y: 
                continue
            self.screen.blit(
                self.textures[enemy.name[0]], (enemy_pixel_x, enemy_pixel_y))
            if enemy.name not in drawn_names:
                enemy_text = self.font.render(f"{enemy.name[0]} = {enemy.name}", True, (0, 0, 0))
                self.screen.blit(enemy_text, (sidebar_x, current_legend_y))
                drawn_names.append(enemy.name)
                current_legend_y += 20

        HP_text = self.font.render(
            f"HP: {self.game.player.hp}/10", True, (0, 0, 0))
        if self.game.player.name == "Remus":
            player_text = self.font.render("@ = Remus", True, (0, 0, 0))

        self.screen.blit(HP_text, (sidebar_x, 5))
        self.screen.blit(player_text, (sidebar_x, 190))

        current_log_y = 50

        for message in self.game.log:
            message_text = self.log_font.render(message, True, (0, 0, 0))
            self.screen.blit(message_text, (sidebar_x, current_log_y))
            current_log_y += 20
