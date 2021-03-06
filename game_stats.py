class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.ships_left = 0
        self.reset_stats()
        self.speed_increase = 1.2
        self.highscore = 0
        self.game_active = False

    def reset_stats(self):
        """ Initialize Statistics that change during the game"""
        self.ships_left = self.settings.ship_limit
        self.game_active = True
        self.score = 0
        self.level = 1

