import textwrap
from entities.level import Level
from entities.player import Player
from entities.enemy import Enemy


class GameLogic:
    """Represents the current game session.

    Attributes:
        game_over: True if the player HP reaches 0.
        game_won: True if the player walks on a door tile.
        log: A list of messages about recent game events.
        level: The current map layout.
        player: The playable character entity.
        enemies: A list of currently active enemy entities.
    """

    def __init__(self):
        """Creates the game session.
        """

        self.game_over = False
        self.game_won = False
        self.log = []
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
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ])
        start_x = 1
        start_y = 1
        self.player = Player(start_x, start_y, hp=10, damage=1, name="Remus")
        self.enemies = []
        self.enemies.append(Enemy(5, 5, hp=3, damage=1, name="Filch"))

    def move_player(self, dx, dy):
        """Handles the turn-based logic of the game. 
        
        Updates the world according to move made by the player.

        Args:
            dx: Move made on the x axis.
            dy: Move made on the y axis.
        """

        new_x, new_y = self.player.get_new_location(dx, dy)
        wall = self.level.is_wall(new_x, new_y)
        door = self.level.is_door(new_x, new_y)
        bumped_enemy = False

        for enemy in self.enemies:
            if enemy.x == new_x and enemy.y == new_y:
                bumped_enemy = True
                enemy.hp -= self.player.damage
                self.add_message(
                    f"Remus attacks {enemy.name}! {enemy.name} has {enemy.hp} HP left.")

                if enemy.hp <= 0:
                    self.enemies.remove(enemy)

                break

        if not wall and not bumped_enemy:
            self.player.move(dx, dy)
            if door:
                self.game_won = True
                self.add_message("Remus escaped! Press Enter to restart.")
                return

        for enemy in self.enemies:
            enemy_new_x, enemy_new_y, move = enemy.get_new_location(
                self.player.x, self.player.y)

            if enemy_new_x == self.player.x and enemy_new_y == self.player.y:
                self.player.hp = max(0, self.player.hp - enemy.damage)
                self.add_message(
                    f"{enemy.name} attacks Remus! Remus has {self.player.hp} HP left.")

            elif not self.level.is_wall(enemy_new_x, enemy_new_y):
                enemy.move(move)

        if self.player.hp <= 0:
            self.game_over = True
            self.add_message("GAME OVER! Press Enter to restart.")

    def add_message(self, text):
        """Handles adding messages about events to the log list. 

        Maintains a maximum length of five messages for the list.

        Args:
            text: Added message as a string.
        """

        wrapped_lines = textwrap.wrap(text, width=45)
        self.log.extend(wrapped_lines)

        while len(self.log) > 5:
            self.log.pop(0)
