import sys
import pygame


class Settings:

    def __init__(self):
        """Initialize the game's static settings."""
        self.screen_height = 1200
        self.screen_width = 800
        self.bg_color = (255, 255, 255)
        self.character_limit = 3
        self.bullet_width = 15
        self.bullet_height = 15
        # self.bullet_color = [60, 60, 60]
        self.bullets_allowed = 3
        self.fleet_drop_speed = 75
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.hinata_speed = 1.0
        self.bullet_speed = 3.0
        self.character_speed = 1.0
        # 1 = right; -1 = left
        self.fleet_direction = 1
        self.hinata_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.hinata_points = int(self.hinata_points * self.score_scale)
        self.hinata_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.character_speed *= self.speedup_scale



