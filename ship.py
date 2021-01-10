import pygame
from settings import Settings as S


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # Load ship rect.
        self.img = pygame.image.load('images/ship.bmp')
        self.rect = self.img.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at its current location    """
        self.screen.blit(self.img, self.rect)
