import sys
import pygame


class Settings:

    def __init__(self):
        self.screen_height = 1200
        self.screen_width = 800
        self.character_speed = 1
        self.character_limit = 3
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 15
        # self.bullet_color = [60, 60, 60]
        self.bullets_allowed = 3
        self.hinata_speed = 1.0
        self.fleet_drop_speed = 120
        # 1 = right; -1 = left
        self.fleet_direction = 1


