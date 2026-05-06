class WorldState:
    def __init__(self):
        self.room = 1
        self.tags = set()
        self.game_over = False
        self.game_won = False
        
    def add_tags(self, tags):
        for tag in tags:
            self.tags.add(tag)
            if tag == "won":
                self.game_won = True
    
    def meets_prerequisites(self, prerequisites):
        for prerequisite in prerequisites:
            if prerequisite not in self.tags:
                return False
        return True