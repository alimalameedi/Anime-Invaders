import sys
import pygame

from naruto import NarutoCharacter
from naruto_background import Background
from settings import Settings


class HeroGame:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode([self.settings.screen_height, self.settings.screen_width])

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Welcome to a hero's journey!")

        self.background = Background('images/1739346.jpg', [0, 0])

        self.character = NarutoCharacter(self)

    def run_game(self):

        while True:
            self._check_event_()
            self.character.update()
            self._update_screen_()

    def _check_event_(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            self._check_down_key_(event)
            self._check_up_key_(event)

    def _check_down_key_(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
            # Move Naruto to the right.
                self.character.moving_right = True

            elif event.key == pygame.K_LEFT:
                self.character.moving_left = True

            elif event.key == pygame.K_q:
                sys.exit()

    def _check_up_key_(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.character.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.character.moving_left = False

    def _update_screen_(self):
        self.screen.fill([255, 255, 255])
        self.screen.blit(self.background.image, self.background.rect)
        self.character.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    new = HeroGame()
    new.run_game()

