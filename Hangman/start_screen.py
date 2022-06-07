# start screen
# 1. start button
# 2. quit button
# 3. title
# 4. instructions


# maybe make a decorator to turn text into buttons
# try make shadows for buttons using a black transparent Surface underneat

import pygame
from pygame.locals import *
from settings_page import SettingsPage


class StartScreen(SettingsPage):
    def __init__(self, game):
        super().__init__(game)
        self.game: Hangman = game

        # boxes
        self.boxes: Dict[str, pygame.Rect] = {
            'game': pygame.Rect(self.game.screen_width // 2 - 50, self.game.screen_height // 10 + 350, 200, 50),
            'settings': pygame.Rect(self.game.screen_width // 2 - 50, self.game.screen_height // 10 + 400, 200, 50),
            'how_to_play': pygame.Rect(self.game.screen_width // 2 - 50, self.game.screen_height // 10 + 450, 200, 50),
            'quit': pygame.Rect(self.game.screen_width // 2 - 50, self.game.screen_height // 10 + 500, 200, 50),
        }

    
    def update(self, mx, my):
        for key, box in self.boxes.items():
            if box.collidepoint(mx, my):
                print("Collision with: " + key)
                if self.game.b1_down:
                    self.game.state = key
                    self.game.b1_down = False
                    break



    def draw(self):

        self.game.button_text(window=self.game.window,
                              x=10, y=10, text='Start', color='red', size=20)

        # title+
        self.game.draw_text(self.game.window,
            self.game.screen_width // 2, self.game.screen_height // 10, 'Hangman', 
            self.colors['white'], size=60, font=self.current_font)
        
        # image
        pygame.draw.rect(self.game.window, self.colors['white'], 
            (self.game.screen_width // 2 - 100, self.game.screen_height // 10 + 60, 
            200, 200), 5, 10)

        # record
        self.game.draw_text(self.game.window,
            self.game.screen_width // 2, self.game.screen_height // 10 + 300,
            'Record: ' + str(self.game.record), self.colors['white'], size=30,
            font=self.current_font)

        # tap to start
        self.game.draw_text(self.game.window,
            self.game.screen_width // 2, self.game.screen_height // 10 + 350,
            'Tap to start', self.colors['white'], size=30,
            font=self.current_font)

        # settings
        self.game.draw_text(self.game.window,
            self.game.screen_width // 2, self.game.screen_height // 10 + 400,
            'Settings', self.colors['white'], size=30,
            font=self.current_font)

        # how to play
        self.game.draw_text(self.game.window,
            self.game.screen_width // 2, self.game.screen_height // 10 + 450,
            'How to play', self.colors['white'], size=30,
            font=self.current_font)

        # quit
        self.game.draw_text(self.game.window,
            self.game.screen_width // 2, self.game.screen_height // 10 + 500,
            'Quit', self.colors['white'], size=30,
            font=self.current_font)

        for box in self.boxes.values():
            pygame.draw.rect(self.game.window, self.colors['white'], box, 5)