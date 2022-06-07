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
from button import Button


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

        # buttons
        self.buttons: Dict[str, Button] = {
            'game': Button(x=self.game.screen_width // 2, y=self.game.screen_height // 10 + 350,
                            text='Start', color='red', size=40, game=self.game),
            'settings': Button(x=self.game.screen_width // 2, y=self.game.screen_height // 10 + 400,
                            text='Settings', color='red', size=40, game=self.game),
            'how_to_play': Button(x=self.game.screen_width // 2, y=self.game.screen_height // 10 + 450,
                            text='How to play', color='red', size=40, game=self.game),
            'quit': Button(x=self.game.screen_width // 2, y=self.game.screen_height // 10 + 500,
                            text='Quit', color='red', size=40, game=self.game),
            'chill': Button(x=self.game.screen_width // 2, y=self.game.screen_height // 10 + 600,
                            text='Chill', color='red', size=40, game=self.game),
        }

    
    def update(self, mx, my):
        for key, button in self.buttons.items():
            if button.is_clicked(mx, my):
                if key == 'game':
                    self.game.state = 'game'
                elif key == 'settings':
                    self.game.state = 'settings'
                elif key == 'how_to_play':
                    self.game.state = 'how_to_play'
                elif key == 'quit':
                    pygame.quit()
                    exit()
                elif key == 'chill':
                    self.game.state = 'chill'

                self.game.b1_down = False
                break
            

    def draw(self):

        # title+
        self.game.draw_text(self.game.window,
            self.game.screen_width // 2, self.game.screen_height // 10, 'Hangman', 
            self.colors['white'], size=60, font=self.current_font)
        
        # image
        pygame.draw.rect(self.game.window, self.colors['white'], 
            (self.game.screen_width // 2 - 100, self.game.screen_height // 10 + 60, 
            200, 200), 5, 10)

        # record, TODO: maybe add a scores page later
        self.game.draw_text(self.game.window,
            self.game.screen_width // 2, self.game.screen_height // 10 + 300,
            'Record: ' + str(self.game.record), self.colors['white'], size=30,
            font=self.current_font)

        # buttons
        for key, button in self.buttons.items():
            button.draw()
        