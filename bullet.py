import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage all bullets fired from ship"""

    def __init__(self, ai_game):
        super().__init__()
        """Create a bullet object at the ship's current location"""
        self.settings = ai_game.settings
        self.color = self.settings.bul_color
        self.screen = ai_game.screen
        # Create bullet rect and set its position.
        self.rect = pygame.Rect(0, 0, self.settings.bul_width, self.settings.bul_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # Control movement.
        self.y = self.rect.y

    def update(self):
        # Move bullet up.
        self.y -= self.settings.bul_speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
