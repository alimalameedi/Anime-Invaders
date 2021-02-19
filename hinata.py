import pygame
from pygame.sprite import Sprite

class Hinata(Sprite):
    """A class for one Hinata in the fleet."""
    def __init__(self, game):
        # Initialize Hinata and set its' starting position.
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/hinata_enemy.bmp')
        self.rect = self.image.get_rect()

        # Start Hinata at the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position for Hinata.
        self.x = float(self.rect.x)

    def update(self):
        """Move Hinata to the right."""
        self.x += (self.settings.hinata_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


