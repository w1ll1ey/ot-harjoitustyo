hallway = {
    "min_width": 16,
    "max_width": 30,
    "min_height": 3,
    "max_height": 7,
    "wall_tile": 1,
    "floor_tile": 0,
    "enemy_pool": ["Filch"]
}

potions_classroom = {
    "min_width": 12,
    "max_width": 25,
    "min_height": 12,
    "max_height": 25,
    "wall_tile": 1,
    "floor_tile": 0,
    "enemy_pool": ["Slughorn", "Snape", "Rat"],
    "lore_pool": ["Advanced Potionsmaking"]
}

gryffindor_dormitory = {
    "min_width": 8,
    "max_width": 12,
    "min_height": 6,
    "max_height": 10,
    "wall_tile": 1,
    "floor_tile": 0,
    "friendly_pool": ["Sirius", "Peter", "James"],
    "lore_pool": ["Record", "Cigarette box", "Lighter"]
}

all_themes = [hallway, potions_classroom, gryffindor_dormitory]