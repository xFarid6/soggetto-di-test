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
from drop_list import DropList


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

        # chill mode
        self.chill_mode: str = 'one'
        self.chill_mode_options: List[str] = ['one', 'two', 'three']

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
        self.toggle_btns: Dict[str, bool] = {
            'fullscreen': [self.fullscreen, ToggleButton(x=self.game.screen_width - 100, y=80+80, state=self.fullscreen, size=30)],
            'sound': [self.sound, ToggleButton(x=self.game.screen_width - 100, y=80+80*2, state=self.sound, size=30)],
            'exclude': [self.exclude, ToggleButton(x=self.game.screen_width - 100, y=80+80*3, state=self.exclude, size=30)]
        }

        # drop_lists
        self.drop_lists: Dict[str, List[str]] = {
            'color_text': [self.text_color, DropList(x=self.game.screen_width - 250, y=80+80*4, options=list(self.colors.keys()), size=30)],
            'color_background': [self.background_color, DropList(x=self.game.screen_width - 250, y=80+80*5, options=list(self.colors.keys()), size=30)],
            'color_button': [self.button_color, DropList(x=self.game.screen_width - 250, y=80+80*6, options=list(self.colors.keys()), size=30)],
            'font': [self.current_font, DropList(x=self.game.screen_width - 250, y=80+80*7, options=self.fonts, size=30)],
            'chill_mode': [self.chill_mode, DropList(x=self.game.screen_width - 250, y=80+80*8, options=self.chill_mode_options, size=30)]
        }
        self.render_order = ['color_text', 'color_background', 'color_button', 'font', 'chill_mode']
        
    
    def update(self, mx, my):
        # track mouse click
        if self.game.b:
            self.game.state = 'start'
            self.game.b = False

        # update toggle buttons
        for key, btn in self.toggle_btns.items():
            state, button = btn
            if button.is_clicked(mx, my) and self.game.b1_down:
                button.state = not button.state
                self.toggle_btns[key][0] = not self.toggle_btns[key][0]
                # print(key, state, button.state)
                self.game.b1_down = False

        # update drop_lists
        for key, drop_list in self.drop_lists.items():
            var, droplist = drop_list
            droplist.update(mx, my)

            if droplist.on_hover(mx, my) and self.game.b1_down:
                droplist.on_click(mx, my)
                self.render_order.insert(-1, self.render_order.pop(self.render_order.index(key)))
            
            if not droplist.on_hover(mx, my):
                droplist.restore()
                # TODO: here should be "self.game.b1_down = False" 
                # but the other droplist would set it to false to stopping the unfnfolding of the current droplist


    def draw(self):
        self.game.draw_text(surf=self.game.window, text='Settings', size=50, x=self.game.screen_width // 2, y=50, color=self.text_color, center=True)
        
        self.game.draw_text(surf=self.game.window, text='B to back', size=20, x=50, y=50, color=self.text_color, center=True)

        c = 0
        for key, value in self.all_settings.items():
            c+=1
            self.game.draw_text(surf=self.game.window, 
                x=15, y=80+80*c, text=' '.join(key.split('_')).capitalize(), 
                color=self.text_color, size=30, center=False)

        for key, btn in self.toggle_btns.items():
            state, button = btn
            button.draw()
    
        for key in self.render_order:
            self.drop_lists[key][1].draw()
