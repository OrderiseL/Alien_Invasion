import pygame.font

class Scoreboard:
    def __init__(self,ai_game):
         self.screen = ai_game.screen
         self.settings = ai_game.settings
         self.stats = ai_game.game_stats
         # Font settings
         self.color = (30,30,30)
         self.font = pygame.font.SysFont(None,48)
         self.prep_score()

    def prep_score(self):
        self.score_rect=0