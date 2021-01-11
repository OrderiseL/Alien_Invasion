import pygame


class Settings:
    # A module to store all settings for objects.
    def __init__(self):
        # Initialize the game's settings.
        self.scr_width = 900
        self.scr_height = 600
        self.bg_color = (0, 0, 5)
        # Ship settings.
        self.ship_speed = 1.5
        # Bullet settings.
        self.bul_color = (80, 80, 80)
        self.bul_speed = 1.0
        self.bul_width = 5
        self.bul_height = 15
