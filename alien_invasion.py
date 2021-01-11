import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.S = Settings()
        self.screen = pygame.display.set_mode((self.S.scr_width, self.S.scr_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion.")

    def run_game(self):
        while True:
            self._check_events()
            # Update objects.
            self.ship.update()
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

    def _keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.right = False
        elif event.key == pygame.K_LEFT:
            self.ship.left = False

    def _update_screen(self):
        """Redraw the screen during each pass"""
        self.screen.fill(self.S.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
