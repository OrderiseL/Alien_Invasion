import pygame
import pygame.font


class Button:
    """A button-like rect that contains text """

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.sc_rect = self.screen.get_rect()
        # Set dimensions and properties of button.
        self.width, self.height = 200, 50
        self.button_color = (30, 30, 30)
        self.text_color = pygame.Color("darkred")
        self.font = pygame.font.SysFont(None, 48)
        # Create background rect and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.sc_rect.center
        # Create text rect.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Render image rect from font with the text
        # and center on background rect.
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)
