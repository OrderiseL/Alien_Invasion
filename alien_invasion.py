import pygame
from time import sleep
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    def __init__(self):
        pygame.init()
        """Initialize main game objects"""
        # Create background objects.
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.scr_width, self.settings.scr_height))
        pygame.display.set_caption("Alien Invasion.")
        self.game_stats = GameStats(self)
        # Create visual objects.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play")
        self.sb = Scoreboard(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            # Update objects(position,values,etc).
            if self.game_stats.game_active:
                self.ship.update()
                self._update_fleet()
                self._update_bullets()
            # Draw on screen.
            self._update_screen()

    def _start_game(self):
        self._reset_objects()
        # Reset statistics.
        self.game_stats.reset_stats()
        self.game_stats.game_active = True
        self.sb.show_score()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)

    def _check_button(self, mouse_pos):
        # Check if play button is pressed
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_stats.game_active:
            pygame.mouse.set_visible(False)
            self._start_game()

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
        if event.key == pygame.K_p:
            self._start_game()

    def _keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.right = False
        elif event.key == pygame.K_LEFT:
            self.ship.left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bul_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and remove old ones"""
        self.bullets.update()
        for bullet in self.bullets.sprites():
            # rid of bullets that are out of screen
            if bullet.rect.bottom < 0:
                bullet.remove(self.bullets)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Check for collisions between aliens and bullets
        and if FLEET has been destroyed"""
        # Check for bullets that collided with aliens.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # Alien shot down -> Increased score
        if collisions:
            for aliens in collisions.values():
                self.game_stats.score += int(self.settings.alien_points) * len(aliens)
            self.sb.prep_score()
            self.sb.check_highscore()
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_fleet(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _ship_hit(self):
        """Lower lives and reset screen"""
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_objects()
        else:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)
        # Pause
        sleep(4)

    def _check_alien_bottom(self):
        # Check if aliens reached the bottom of the screen.
        for alien in self.aliens.sprites():
            if alien.rect.bottom > self.settings.scr_height:
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create the fleet of Aliens"""
        # We'll create a new alien to figure out how many aliens
        # can fit in a row.
        new_alien = Alien(self)
        a_width, a_height = new_alien.rect.size
        available_space_x = self.settings.scr_width - (2 * a_width)
        amount_in_row = available_space_x // (2 * a_width) - 2
        # Calculate amount of rows.
        available_space_y = (self.settings.scr_height -
                             self.ship.rect.height - 3 * a_height)
        amount_of_rows = available_space_y // (3 * a_height) + 1
        # Add aliens to fleet.
        for row in range(amount_of_rows):
            for al_number in range(amount_in_row):
                self._create_alien(al_number, row)

    def _create_alien(self, alien_number, row_num):
        new_alien = Alien(self)
        a_width, a_height = new_alien.rect.size
        # Aliens' X position.
        new_alien.x = new_alien.x + 2 * a_width * alien_number
        new_alien.rect.x = new_alien.x
        # Aliens' Y position.
        new_alien.rect.y = new_alien.rect.y + 2 * a_height * row_num
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if (alien.rect.right > self.settings.scr_width
                    or alien.rect.left < 0):
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        self.settings.fleet_direction *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

    def _update_screen(self):
        """Redraw the screen during each pass"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        # Game paused.
        if not self.game_stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
        # Check alien-ship collision.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Check if aliens reached bottom.
        self._check_alien_bottom()

    def _reset_objects(self):
        # Get rid of any remaining aliens and bullets.
        self.bullets.empty()
        self.aliens.empty()
        self.settings.init_dynamic_settings()
        # Place ship at start and create a new fleet.
        self.ship.rect.midbottom = self.screen.get_rect().midbottom
        self.ship.x = float(self.ship.rect.x)
        self._create_fleet()
        # Reset dynamic settings.
        self.settings.init_dynamic_settings()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
