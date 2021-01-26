import pygame


class Settings:
    # A module to store all settings for objects.
    def __init__(self):
        # Initialize the game's static settings.
        self.scr_width = 1000
        self.scr_height = 650
        self.bg_color = (230, 230, 230)
        # Ship settings.
        self.ship_limit = 3
        # Bullet settings.
        self.bul_color = (50, 50, 50)
        self.bul_width = 5
        self.bul_height = 15
        self.bul_allowed = 3
        # Alien settings.
        self.speedup_factor = 1.2
        self.fleet_drop_speed = 10
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Settings that change during game"""
        self.fleet_direction = 1  # 1=RIGHT -1=LEFT.
        self.alien_speed = 0.5
        self.bul_speed = 1.0
        self.ship_speed = 1.0
        self.alien_points = 10

    def increase_speed(self):
        self.alien_speed *= self.speedup_factor
        self.bul_speed *= self.speedup_factor
        self.ship_speed *= self.speedup_factor
        self.alien_points *= 1.2
