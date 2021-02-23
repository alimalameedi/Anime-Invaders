class GameStats:
    """Track the statistics for Alien Invasion."""

    def __init__(self, game):
        """Initialize statistics."""
        self.settings = game.settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.characters_remaining = self.settings.character_limit
        self.score = 0


