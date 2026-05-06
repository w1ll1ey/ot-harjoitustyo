class WorldState:
    def __init__(self):
        self.room = 1
        self.tags = set()
        
    def add_tags(self, tags):
        for tag in tags:
            self.tags.add(tag)
    
    def meets_prerequisites(self, prerequisites):
        for prerequisite in prerequisites:
            if prerequisite not in self.tags:
                return False
        return True