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
import string
from typing import List, Dict, Optional
import random


class GameScreen(SettingsPage):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.window = pygame.display.get_surface()
        self.settings = SettingsPage(self.game)
        self.font = self.settings.current_font

        # buttons
        self.clue = Button(x=self.game.screen_width - 100, y=50, 
            text='Clue', size=15, color='white', game=self.game)

        # hagman image
        self.hangman = pygame.Surface(size=(self.game.screen_width - 100, self.game.screen_height//2 - 100), flags=SRCALPHA)
        self.hangman.fill((255, 255, 255, 30))
        self.hm_rect = self.hangman.get_rect()
        self.hm_rect.center = (self.game.screen_width//2, self.game.screen_height//2 - 100)

        # letters
        self.alphabet = list(string.ascii_uppercase)
        self.key_size = 50
        self.keyboard: Dict[str, Button] = {}
        for i, letter in enumerate(self.alphabet):
            self.keyboard[letter] = Button(x= 150 + int(i%7) * self.key_size,
                y=self.game.screen_height//2 + 150 + (self.key_size*int(i//7)+1), text=letter, size=40, color='white', game=self.game, shadow=False)

        # guessing
        # load the game variables
        self.win = False
        self.score: int = 0
        self.word: str = self.pick_word().upper()
        self.word_state: List[str] = ['_'] * len(self.word)
        self.letters_removed: set = set(self.word)
        self.guessed: set = set()


    def pick_word(self) -> str: 
        return random.choice(self.game.words)


    def give_clue(self):
        letter = None
        while (letter in self.guessed) or (not letter in self.letters_removed):
            letter = random.choice(self.word)
        self.guessed.add(letter)
        self.keyboard[letter].color = 'Purple'

    def reset(self):
        self.win = False
        self.word = self.pick_word().upper()
        self.word_state = ['_'] * len(self.word)
        self.letters_removed = set(self.word)
        self.guessed = set()
        for letter in self.alphabet:
            self.keyboard[letter].color = 'white'


    def update(self, mx, my): 
        if ''.join(self.word_state) == self.word:
            self.win = True
            self.score += 1
            c = 0
            surf = pygame.Surface(size=(self.game.screen_width, self.game.screen_height), flags=SRCALPHA)
            surf.fill((255, 100, 100, 30))
            while c < 100:
                c += 1
                self.game.draw_text(surf=surf, text='You win!', x=self.game.screen_width//2, y=self.game.screen_height//2, color=(255, 230, 230, 255))
                self.game.window.blit(surf, (0, 0))
                pygame.display.flip()
                self.game.clock.tick(60)
            self.reset()
                

        if self.game.b:
            self.game.state = 'start'
        if self.game.q:
            pygame.quit()
            exit()
        if self.game.r:
            self.reset()

        if self.clue.is_clicked(mx, my):
            if self.word != ''.join(self.word_state):
                self.give_clue()

        for letter in self.alphabet:
            if self.keyboard[letter].is_clicked(mx, my):
                self.keyboard[letter].color = 'Purple'
                self.guessed.add(letter)
        for i, letter in enumerate(self.word):
            if letter in self.guessed:
                self.word_state[i] = letter


    def draw(self, window=None):
        if window is None:
            window = self.window

        # top text
        self.game.draw_text(window, 40, 10, 'B to back', 'white', 20, 'arial', True, True)
        self.game.draw_text(window, 40, 40, 'Q to quit', 'white', 20, 'arial', True, True)
        self.game.draw_text(window, 40, 70, 'R to reset', 'white', 20, 'arial', True, True)
        self.game.draw_text(window, self.game.screen_width//2, 50, 'Hangman', 'white', 40, 'arial', True, True)

        self.clue.draw()

        # hangman representation
        window.blit(self.hangman, self.hm_rect)

        # keyboard
        for letter in self.alphabet:
            self.keyboard[letter].draw()

        # word
        self.game.draw_text(window, self.game.screen_width//2, self.game.screen_height//2 + 100, ' '.join(self.word_state), 'white', 40, 'arial', True, True)

        # score
        self.game.draw_text(window, self.game.screen_width//2, 100, f'Score: {self.score}', 'white', 40, 'arial', True, True)
