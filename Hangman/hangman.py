import pygame
from pygame.locals import *
import random
import os
from typing import List

from game_screen import GameScreen
from settings_page import SettingsPage
from how_to_play import HowToPlay
from start_screen import StartScreen


'''
    This is the main file for the hangman game.
    It will be responsible for the game loop,
    and the main game logic.

    The game will be played in a window,
    and will be able to be played in fullscreen.
'''


class Hangman:
    def __init__(self) -> None:
    # initialize pygame
        pygame.init()
        self.path: str = os.path.dirname(__file__) + '\\'

    # load the window
        self.screen_width: int = 600
        self.screen_height: int = 800
        self.window: pygame.Surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Hangman')
        self.clock: pygame.time.Clock = pygame.time.Clock()

    # load the sounds
        pygame.mixer.init()
    
    # load the images
        # self.background_forest: List[pygame.Surface] = [pygame.image.load(self.path + "Background-layers\\" + file).convert_alpha() for file in os.listdir(self.path+"Background-layers") if '05' not in file]
        # self.backgrounds: List[pygame.Surface] = [pygame.image.load(self.path + "Background-forest-jpg\\" + file).convert_alpha() for file in os.listdir(self.path+"Background-forest-jpg")]
        # self.pngs: List[pygame.Surface] = [pygame.image.load(self.path + "jpg2png\\" + file).convert_alpha() for file in os.listdir(self.path+"jpg2png")]

    # load the words
        self.words: List[str] = []

    # load the game objects
        self.start_screen: StartScreen = StartScreen(self)
        self.settings_page: SettingsPage = SettingsPage(self)
        self.game_screen: GameScreen = GameScreen(self)
        self.how_to_play: HowToPlay = HowToPlay(self)

    # load the game state
        self.state: str = 'start'
        self.all_states: Dict[str, object] = {
            'start': StartScreen(self),
            'game': GameScreen(self),
            'settings': SettingsPage(self),
            'how_to_play': HowToPlay(self)
        }

    # load the game variables
        self.record: int = 0
        self.score: int = 0
        self.time: int = 0
        self.word: str = ''
        self.letters: List[str] = []
        self.hangman: int = 0
        self.guessed: List[str] = []
        self.correct: List[str] = []
        self.incorrect: List[str] = []

    # mouse
        self.b1_down: bool = False


    def button(original_draw):
        def draw_rect(*args, **kwargs):
            surf = pygame.Surface((kwargs['size']//2 * len(kwargs['text']) + kwargs['size'], kwargs['size'] * 2), 0, 32)
            surf.fill((255, 200, 255))
            win = kwargs['window']
            kwargs['window'] = surf

            pygame.draw.rect(surf, 'red', (0, 0, kwargs['size']//2 * len(kwargs['text']) + kwargs['size'], kwargs['size'] * 2), 3, 0, 5, 5, 5)
            original_draw(*args, **kwargs)

            shadow = pygame.Surface((kwargs['size']//2 * len(kwargs['text']) + kwargs['size'], kwargs['size'] * 2), 0, 32)
            shadow.fill((0, 0, 0))
            shadow.set_alpha(100)
            win.blit(shadow, (kwargs['x'] + 5, kwargs['y'] + 5))

            win.blit(surf, (kwargs['x'], kwargs['y']))

        return draw_rect

    @button
    def button_text(self, window, x, y, text, color, size, font='arial', center=True, aa=True, shadow=True) -> None:
        font = pygame.font.SysFont(font, size)
        text = font.render(text, aa, color)

        text_rect = text.get_rect()
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)

        window.blit(text, text_rect)

    def draw_text(self, surf, x, y, text, color, size=30, font='arial', center=True, aa=True, shadow=True) -> None:
        font = pygame.font.SysFont(font, size)
        text = font.render(text, aa, color)

        text_rect = text.get_rect()
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)

        surf.blit(text, text_rect)


    def update(self) -> None:
        self.all_states[self.state].update(self.mx, self.my)


    def draw(self) -> None:
        self.window.fill(self.all_states['settings'].colors['default grey'])
        self.all_states[self.state].draw()

        pygame.display.flip()


    def get_events(self) -> None:
        self.mx, self.my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.button, f'({self.mx=}, {self.my=})')
                if event.button == 1:
                    self.b1_down = True


    def run(self) -> None:
        while True:
            self.clock.tick(30)
            self.get_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game: Hangman = Hangman()
    game.run()
