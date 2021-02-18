import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.image = pygame.image.load('images/Shuriken.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = game.character.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed

        # Update the rect position.
        self.rect.y = self.y

    def blit_bullet(self):
        """Draw bullet to screen."""
        self.screen.blit(self.image, self.rect)

