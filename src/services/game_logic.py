import random
import textwrap
from entities.level import Level
from data.level_themes import all_themes
from entities.player import Player
from entities.enemy import Enemy
from entities.friendly import Friendly
from data.hostile_mobs import hostile_mobs
from data.lore_deck import lore_items
from data.lore_deck import friendlys
from data.lore_deck import dialogue_tree


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

    def __init__(self, world_state):
        """Creates the game session.
        """

        self.world_state = world_state
        self.room = world_state.room
        self.game_over = False
        self.game_won = False
        self.log = []
        
        self.generate_room()
        
        self.player = Player(self.level.player_spawn[0], self.level.player_spawn[1], hp=10, damage=1, name="Remus")
        
    def generate_room(self):
        self.theme = random.choice(all_themes)
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
                hp = stats["hp"], 
                damage = stats["damage"], 
                name = enemy_name
            ))
        
        raw_lore_pool = self.theme.get("lore_pool", [])
        self.lore_pool = []
        for lore in raw_lore_pool:
            if self.world_state.meets_prerequisites(lore_items[lore]["prerequisites"]):
                self.lore_pool.append(lore)
        if len(self.lore_pool) > 0:
            self.level.matrix[spawnpoints[0][1]][spawnpoints[0][0]] = 3
            
        raw_friendly_pool = self.theme.get("friendly_pool", [])
        self.friendly_pool = []
        for friendly in raw_friendly_pool:
            if self.world_state.meets_prerequisites(friendlys[friendly]["prerequisites"]):
                self.friendly_pool.append(friendly)
        
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
                hp = 0,
                damage = 0,
                name = friendly_name,
                dialogue = chosen_dialogue,
                tags = tags
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
            dx: Move made on the x axis.
            dy: Move made on the y axis.
        """

        new_x, new_y = self.player.get_new_location(dxdy)
        wall = self.level.is_wall(new_x, new_y)
        door = self.level.is_door(new_x, new_y)
        lore = self.level.is_lore(new_x, new_y)
        bumped_entity = False
        
        for friendly in self.friendlys:
            if friendly.x == new_x and friendly.y == new_y:
                bumped_entity = True
                self.add_message(friendly.dialogue)
                if len(friendly.tags) > 0:
                    self.world_state.add_tags(friendly.tags)
                
                break

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