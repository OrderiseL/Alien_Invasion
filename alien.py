import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        """Initialize alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load image and get its rect.
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        # Set starting position at top left while keeping a space.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Use a float variable for accuracy.
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x

