# settings page
# 1. back button
# 2. fullscreen toggle
# 3. sound toggle
# 4. optional wordlist exclude toggle
# 5. color changes

import pygame
from pygame.locals import *
from typing import List, Any, Dict

from toggle_button import ToggleButton


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

        # buttons

        # all settings
        self.all_settings: Dict[str, str] = {
            'fullscreen': 'toggle',
            'sound': 'toggle',
            'exclude': 'toggle',
            'color_text': 'drop_list',
            'color_background': 'drop_list',
            'color_button': 'drop_list',
            'font': 'drop_list',
            'chill_mode': 'drop_list'
        }

        # buttons
        self.toggle_button_dict: Dict[str, bool] = {
            'fullscreen': self.fullscreen,
            'sound': self.sound,
            'exclude': self.exclude
        }

        self.toggle_btns: List[ToggleButton] = [
            ToggleButton(x=self.game.screen_width - 100, y=80+80*(c+1), state=self.toggle_button_dict.get(key), size=30)
            for c, key in enumerate(self.toggle_button_dict.keys())]
        
    
    def update(self, mx, my):
        if self.game.b:
            self.game.state = 'start'
            self.game.b = False

        for btn in self.toggle_btns:
            if btn.is_clicked(mx, my) and self.game.b1_down:
                btn.state = not btn.state
                self.game.b1_down = False
                # self.toggle_button_dict[btn.text.lower()] = btn.state


    def draw(self):
        self.game.draw_text(surf=self.game.window, text='Settings', size=50, x=self.game.screen_width // 2, y=50, color=self.text_color, center=True)
        
        self.game.draw_text(surf=self.game.window, text='B to back', size=20, x=50, y=50, color=self.text_color, center=True)

        c = 0
        for key, value in self.all_settings.items():
            c+=1
            self.game.draw_text(surf=self.game.window, 
                x=15, y=80+80*c, text=' '.join(key.split('_')).capitalize(), 
                color=self.text_color, size=30, center=False)

        for btn in self.toggle_btns:
            btn.draw()
