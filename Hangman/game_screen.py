# game screen
# 1. word
# 2. letters
# 3. hangman
# 4. score
# 5. time
# 6. quit button

import pygame
from pygame.locals import *
from settings_page import SettingsPage
from button import Button

class GameScreen(SettingsPage):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.window = pygame.display.get_surface()

        # buttons
        self.clue = Button(x=self.game.screen_width - 100, y=50, 
            text='Clue', size=15, color='white', game=self.game)

    
    def update(self, mx, my): 
        pass


    def draw(self, window=None):
        if window is None:
            window = self.window
        self.game.draw_text(window, 40, 10, 'B to back', 'white', 20, 'arial', True, True)
        self.game.draw_text(window, 40, 40, 'Q to quit', 'white', 20, 'arial', True, True)
        self.game.draw_text(window, self.game.screen_width//2, 50, 'Hangman', 'white', 40, 'arial', True, True)

        self.clue.draw()
