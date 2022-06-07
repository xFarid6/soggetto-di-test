# game screen
# 1. word
# 2. letters
# 3. hangman
# 4. score
# 5. time
# 6. quit button
# 7. settings button

import pygame
from pygame.locals import *
from settings_page import SettingsPage


class GameScreen(SettingsPage):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
