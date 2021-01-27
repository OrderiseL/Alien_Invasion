import pygame.font
from ship import Ship


class Databoard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.scr_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.game_stats
        # Font settings
        self.color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        self.score_str = "{:,}".format(self.stats.score)
        self.score_img = self.font.render(self.score_str, True,
                                          self.color, self.settings.bg_color)
        # Display the score at the top right corner.
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.scr_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        # Create level objects.
        lvl_str = str(self.stats.level)
        self.lvl_image = self.font.render(lvl_str, True, (0, 200, 0))
        self.lvl_rect = self.lvl_image.get_rect()
        # Position on display
        self.lvl_rect.midtop = self.score_rect.midbottom
        self.lvl_rect.y += 10

    def prep_ships(self):
        self.ships = []
        for ship_num in range(self.stats.ships_left):
            nship = Ship(self.ai_game)
            nship.img = pygame.transform.scale(nship.img, (45, 30))
            nship.rect.topleft = self.scr_rect.topleft
            nship.rect.x += nship.rect.width*ship_num
            self.ships.append(nship)

    def prep_highscore(self):
        # Create Highscore image
        highscore_str = "{:,}".format(int(self.stats.highscore))
        self.highscore_img = self.font.render(highscore_str, True, (200, 50, 50))
        self.highscore_rect = self.highscore_img.get_rect()
        # Position rect at top middle.
        self.highscore_rect.midtop = self.scr_rect.midtop

    def check_highscore(self):
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prep_highscore()

    def show_datas(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.highscore_img, self.highscore_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        for ship in self.ships:
            ship.blitme()