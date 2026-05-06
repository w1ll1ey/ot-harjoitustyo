from entities.character import Character

class Friendly(Character):
    def __init__(self, start_x, start_y, *, hp, damage, name, dialogue, tags):
        super().__init__(start_x, start_y, hp=hp, damage=damage, name=name)
        self.dialogue = dialogue
        self.tags = tags
    