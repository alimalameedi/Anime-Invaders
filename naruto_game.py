import sys
import pygame

from naruto import NarutoCharacter
from naruto_background import Background
from settings import Settings
from shuriken import Bullet
from hinata import Hinata


class HeroGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode([self.settings.screen_height, self.settings.screen_width])

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Welcome to Naruto's journey to Hokage!")
        self.background = Background('images/1739346.jpg', [0, 0])
        self.character = NarutoCharacter(self)
        self.bullets = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):

        while True:
            self._check_event_()
            self.character.update()
            self._update_bullets()
            self._update_hinata()
            self._update_screen_()

    def _create_fleet(self):
        """Create fleet of Hinata!"""
        hinata_enemy = Hinata(self)
        enemy_width, enemy_height = hinata_enemy.rect.size
        available_space_x = self.settings.screen_width - (2 * enemy_width)
        number_enemies_x = available_space_x // (2 * enemy_width)

        naruto_height = self.character.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * enemy_height) - naruto_height)
        number_rows = available_space_y // (5 * enemy_height)

        for row_number in range(number_rows):
            for enemies in range(number_enemies_x):
                self._create_enemies(enemies, row_number)

    def _create_enemies(self, enemies, row_number):
            hinata_enemy = Hinata(self)
            enemy_width, enemy_height = hinata_enemy.rect.size
            hinata_enemy.x = enemy_width + 2 * enemy_width * enemies
            hinata_enemy.rect.x = hinata_enemy.x
            hinata_enemy.rect.y = hinata_enemy.rect.height + 2 * hinata_enemy.rect.height * row_number
            self.enemy.add(hinata_enemy)


    def _check_fleet_edges(self):
        """Respond appropriately if Hinata reaches an edge."""
        for hinata in self.enemy.sprites():
            if hinata.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for hinata in self.enemy.sprites():
            hinata.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

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

            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_up_key_(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.character.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.character.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group. Limits to 3 shuriken per screen until they disappear."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen_(self):
        self.screen.fill([255, 255, 255])
        self.screen.blit(self.background.image, self.background.rect)
        self.character.blitme()

        for bullet in self.bullets.sprites():
            bullet.blit_bullet()

        self.enemy.draw(self.screen)

        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_hinata(self):
        """Check if fleet is at an edge,
             then update the positions of all Hinata in the fleet!
        """
        self._check_fleet_edges()
        self.enemy.update()


if __name__ == '__main__':
    new = HeroGame()
    new.run_game()

