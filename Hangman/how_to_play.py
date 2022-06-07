# how to play page
# 1. back button
# 2. instructions


import pygame 
from pygame.locals import *
from settings_page import SettingsPage
from button import Button


class HowToPlay(SettingsPage):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        
        self.instructions: str = '''
        How to play:
        1. Select a word from the word list.
        2. Guess letters by pressing the corresponding keys.
        3. If you guess the word correctly, you win!
        4. If you guess the word incorrectly, you lose!
        5. You can quit the game at any time by pressing the quit button.
        6. You can change the settings at any time by pressing the settings button.
        '''

        self.back_button = Button(x=60, y=60, text='Back', color=self.colors['dark_emerald'], size=50, game=self.game)


    def update(self, mx, my):
        pass


    def draw(self):
        for i, line in enumerate(self.instructions.splitlines()):
            self.game.draw_text(self.game.window,
                2, self.game.screen_height // 10 * (i+1), line, 
                self.colors['white'], size=20, font=self.current_font, center=False)

        self.back_button.draw(self.game.window)

