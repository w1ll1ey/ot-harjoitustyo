import random
import textwrap

from entities.level import Level
from entities.player import Player
from entities.enemy import Enemy
from entities.friendly import Friendly

from data.level_themes import all_themes
from data.hostile_mobs import hostile_mobs
from data.lore_deck import lore_items
from data.lore_deck import friendlys
from data.lore_deck import dialogue_tree


class GameLogic:
    """Represents the current game session. Controls the game state and turn-based engine.

    Attributes:
        world_state: State containing and handling the procedural narrative.
        log: A list of messages about recent game events.
        level: The current room layout.
        player: The playable character entity.
        enemies: A list of currently active enemy entities.
        friendlys: A list of currently active non-hostile entities.
        theme: Theme used to generate the current room.
        lore_pool: Available lore items in the current room.
        friendly_pool: Available non-hostile entities in the current room.
    """

    def __init__(self, world_state, level=None, player=None):
        """Creates the game session.

        Args:
            world_state: State containing and handling the procedural narrative.
            level: Optional pre-built level, currently used only for testing.
            player: Optional pre-built player entity, currently used only for testing.
        """

        self.world_state = world_state
        self.log = []

        if level:
            self.level = level
            self.enemies = []
            self.friendlys = []

        else:
            self.generate_room()

        if player:
            self.player = player

        else:
            self.player = Player(
                self.level.player_spawn[0], self.level.player_spawn[1],
                hp=10, damage=1, name="Remus")

    def generate_room(self):
        filtered_themes = []
        for theme in all_themes:
            if self.world_state.room >= theme["min_room_number"]:
                filtered_themes.append(theme)
        self.theme = random.choice(filtered_themes)
        self.level = Level(self.theme)
        self.enemies = []
        self.friendlys = []

        spawnpoints = random.sample(self.level.free_tiles, 3)
        enemy_pool = self.theme.get("enemy_pool", [])

        if len(enemy_pool) > 0:
            enemy_name = random.choice(enemy_pool)
            stats = hostile_mobs[enemy_name]
            self.enemies.append(Enemy(
                spawnpoints[1][0],
                spawnpoints[1][1],
                hp=stats["hp"],
                damage=stats["damage"],
                name=enemy_name
            ))

        raw_lore_pool = self.theme.get("lore_pool", [])
        self.lore_pool = []
        for lore in raw_lore_pool:
            if self.world_state.meets_prerequisites(lore_items[lore]["prerequisites"]):
                not_collected = True
                for tag in lore_items[lore]["tags"]:
                    if tag in self.world_state.tags:
                        not_collected = False
                        break
                if not_collected:
                    self.lore_pool.append(lore)
        if len(self.lore_pool) > 0:
            self.level.matrix[spawnpoints[0][1]][spawnpoints[0][0]] = 3

        raw_friendly_pool = self.theme.get("friendly_pool", [])
        self.friendly_pool = []
        for friendly in raw_friendly_pool:
            if self.world_state.meets_prerequisites(friendlys[friendly]["prerequisites"]):
                self.friendly_pool.append(friendly)
                if len(friendlys[friendly]["tags"]) > 0:
                    self.world_state.add_tags(friendlys[friendly]["tags"])

        if len(self.friendly_pool) > 0:
            friendly_name = random.choice(self.friendly_pool)
            for dialogue in dialogue_tree[friendly_name].values():
                if self.world_state.meets_prerequisites(dialogue["prerequisites"]):
                    chosen_dialogue = dialogue["text"]
                    tags = dialogue["tags"]

                    break

            self.friendlys.append(Friendly(
                spawnpoints[2][0],
                spawnpoints[2][1],
                hp=0,
                damage=0,
                name=friendly_name,
                dialogue=chosen_dialogue,
                tags=tags
            ))

    def next_room(self):
        self.world_state.room += 1

        self.generate_room()

        self.player.x = self.level.player_spawn[0]
        self.player.y = self.level.player_spawn[1]

    def move_player(self, dxdy):
        """Handles the turn-based logic of the game. 

        Updates the world according to move made by the player.

        Args:
            dxdy: Tuple (dx, dy) containing the move made on x and y axis.
        """

        new_x, new_y = self.player.get_new_location(dxdy)
        wall = self.level.is_wall(new_x, new_y)
        door = self.level.is_door(new_x, new_y)
        lore = self.level.is_lore(new_x, new_y)
        bumped_entity = False

        for friendly in self.friendlys:
            friendly_new_x, friendly_new_y, friendly_move = friendly.get_new_location()

            if (friendly.x == new_x and friendly.y == new_y
                    or friendly_new_x == new_x and friendly_new_y == new_y):
                bumped_entity = True
                self.add_message(friendly.dialogue)
                if len(friendly.tags) > 0:
                    self.world_state.add_tags(friendly.tags)

                continue

            if not self.level.is_wall(friendly_new_x, friendly_new_y):
                friendly.move(friendly_move)

        for enemy in self.enemies:
            if enemy.x == new_x and enemy.y == new_y:
                bumped_entity = True
                enemy.hp -= self.player.damage
                self.add_message(
                    f"Remus attacks {enemy.name}! {enemy.name} has {enemy.hp} HP left.")

                if enemy.hp <= 0:
                    self.enemies.remove(enemy)

                break

        if not wall and not bumped_entity:
            self.player.move(dxdy)
            if door:
                self.next_room()
                return
            if lore:
                lore_name = random.choice(self.lore_pool)
                self.add_message(lore_items[lore_name]["text"])
                if len(lore_items[lore_name]["tags"]) > 0:
                    self.world_state.add_tags(lore_items[lore_name]["tags"])
                self.level.matrix[new_y][new_x] = 0

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
            self.world_state.game_over = True
            self.add_message("GAME OVER! Press Enter to restart.")

    def add_message(self, text):
        """Handles adding messages about events to the log list. 

        Maintains a maximum length of five messages for the list.

        Args:
            text: Added message as a string.
        """

        wrapped_lines = textwrap.wrap(text, width=40)
        self.log.extend(wrapped_lines)

        while len(self.log) > 6:
            self.log.pop(0)
