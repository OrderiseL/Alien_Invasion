import pygame
from settings import Settings as S


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.S
        self.screen_rect = self.screen.get_rect()
        # Load ship rect.
        self.img = pygame.image.load('images/ship.bmp').convert()
        self.img.set_colorkey((230, 230, 230))
        self.rect = self.img.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        # Control ships position.
        self.x = float(self.rect.x)

        # Movement.
        self.left = False
        self.right = False

    def update(self):
        if self.right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_x
        if self.left and self.rect.left > 0:
            self.x -= self.settings.ship_x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location    """
        self.screen.blit(self.img, self.rect)
