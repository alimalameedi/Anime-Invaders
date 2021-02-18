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

