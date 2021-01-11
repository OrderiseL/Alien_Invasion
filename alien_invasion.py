import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    def __init__(self):
        pygame.init()
        """Initialize main game objects"""
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.scr_width, self.settings.scr_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion.")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            # Update objects(position,values,etc).
            self.ship.update()
            self.bullets.update()
            # Draw on screen.
            self._update_screen()

    def _check_events(self):
        """Respond to keypress and mouse input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle player keypress.
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.right = True
        elif event.key == pygame.K_LEFT:
            self.ship.left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.right = False
        elif event.key == pygame.K_LEFT:
            self.ship.left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Redraw the screen during each pass"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom < 0:
                bullet.remove(self.bullets)
            else:
                bullet.draw()
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
