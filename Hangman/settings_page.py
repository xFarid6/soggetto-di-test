# settings page
# 1. back button
# 2. fullscreen toggle
# 3. sound toggle
# 4. optional wordlist exclude toggle
# 5. color changes

import pygame
from pygame.locals import *


class SettingsPage:
    def __init__(self, game):
        self.game = game
        self.fullscreen: bool = False
        self.sound: bool = True
        self.exclude: bool = False
        self.color: str = 'white'

        # colors
        self.colors: Dict[str, tuple] = {
            'default grey': (30, 30, 30),
            'white': (255, 255, 255),
            'black': (0, 0, 0),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'cyan': (0, 255, 255),
            'magenta': (255, 0, 255),
            'gray': (128, 128, 128),
            'dark_gray': (64, 64, 64),
            'light_gray': (192, 192, 192),
            'dark_red': (128, 0, 0),
            'dark_green': (0, 128, 0),
            'dark_blue': (0, 0, 128),
            'dark_yellow': (128, 128, 0),
            'dark_cyan': (0, 128, 128),
            'dark_magenta': (128, 0, 128),
            'dark_orange': (255, 128, 0),
            'dark_purple': (128, 0, 128),
            'dark_pink': (255, 0, 128),
            'dark_brown': (128, 64, 0),
            'dark_teal': (0, 128, 128),
            'dark_lavender': (128, 0, 255),
            'dark_turquoise': (0, 128, 255),
            'dark_emerald': (0, 255, 128),
            'dark_navy': (0, 64, 128),
            'dark_maroon': (64, 0, 64),
            'dark_teal': (0, 64, 128),
            'dark_lime': (64, 128, 0),
            'dark_violet': (64, 0, 255),
        }
        self.text_color = self.colors['white']
        self.background_color = self.colors['default grey']
        self.button_color = self.colors['dark_orange']

        # fonts
        self.fonts: List[str] = pygame.font.get_fonts()
        self.current_font: str = self.fonts[0]

    
    def update(self, mx, my):
        pass


    def draw(self):
        pass