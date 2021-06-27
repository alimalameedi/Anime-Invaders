import pygame.font
from pygame.sprite import Group
from naruto import NarutoCharacter

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, game):
        """Initialize scorekeeping attributes."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.prep_narutos()

        # Font settings for scores
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
       # score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color)

        # Display score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""

        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.narutos.draw(self.screen)

    def check_high_score(self):
        """Check to see if there's a new highscore"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        # add str("High Score: ") + below and subsequently if I need to add text to screen for labels
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                                            self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_narutos(self):
        """Show how many ships are left."""
        self.narutos = Group()
        for naruto_number in range(self.stats.characters_remaining):
            naruto = NarutoCharacter(self.game)
            naruto.rect.x = 10 + naruto_number * naruto.rect.width
            naruto.rect.y = 10
            self.narutos.add(naruto)



