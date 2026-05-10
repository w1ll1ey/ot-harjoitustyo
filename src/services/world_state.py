class WorldState:
    """Class containing information about the state of the world.

    Stores information between rooms and gives GameLogic data for procedural narrative.

    Attributes:
        room: Current room number.
        tags: Set of collected progression tags.
        game_over: True if the player has died.
        game_won: True if the win condition has been reached.
    """

    def __init__(self):
        """Creates the world state.
        """

        self.room = 1
        self.tags = set()
        self.game_over = False
        self.game_won = False

    def add_tags(self, tags):
        """Adds progression tags to the world state.

        Args:
            tags: List of tags to add.
        """

        for tag in tags:
            self.tags.add(tag)
            if tag == "won":
                self.game_won = True

    def meets_prerequisites(self, prerequisites):
        """Checks if the required tags have been collected.

        Args:
            prerequisites: List of required tags.

        Returns:
            True if all required tags have been collected, False if not.
        """

        for prerequisite in prerequisites:
            if prerequisite not in self.tags:
                return False
        return True
