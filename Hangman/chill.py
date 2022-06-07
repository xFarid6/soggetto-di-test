import pygame
import random
from settings_page import SettingsPage


class Chill(SettingsPage):
    def __init__(self, game): 
        super().__init__(game)
        self.game = game
        self.center = (self.game.screen_width // 2, self.game.screen_height // 2)

    def update(self, mx, my): 
        if self.game.b:
            self.game.state = 'start'
            self.game.b = False

    def draw(self):
        # drop white particles from the center of the screen
        for i in range(random.randint(10, 20)):
            pygame.draw.circle(self.game.window, self.colors['white'],
                               (random.randint(self.game.screen_width // 2 - 200, self.game.screen_width // 2 + 200),
                                random.randint(self.game.screen_height // 2 - 200, self.game.screen_height // 2 + 200)),
                               random.randint(0, 5))

        self.game.clock.tick(2)
