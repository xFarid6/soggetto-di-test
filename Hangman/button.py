import pygame
from settings_page import SettingsPage

class Button:
    def __init__(self, x, y, text, color, size, game, font='arial', center=True, aa=True, shadow=True):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = size
        self.font = font
        self.center = center
        self.aa = aa
        self.shadow = shadow

        self.width = len(text) * size
        self.height = size 
        self.window = pygame.display.get_surface()

        self.game = game
        self.settings = SettingsPage(self.game)


    def clicked(self, mx, my):
        if self.x <= mx <= self.x + self.size and self.y <= my <= self.y + self.size:
            return True
        return False

    
    def draw(self, window=None):
        if window is None:
            window = self.window
        
        # shadow
        if self.shadow:
            shadow_surf = pygame.Surface((self.width, self.height), 0, 32)
            shadow_surf.fill((0, 0, 0))
            shadow_surf.set_alpha(100)
            if self.center:
                window.blit(shadow_surf, (self.x + 5 - self.width//2, self.y + 5 - self.height//2))
            else:
                window.blit(shadow_surf, (self.x + 5, self.y + 5))

        # button
        button_surf = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.center:
            button_surf.center = (self.x, self.y)
            pygame.draw.rect(window, self.settings.button_color, button_surf, width=0,
                border_top_left_radius=8, border_top_right_radius=8, 
                border_bottom_left_radius=8, border_bottom_right_radius=0)
        else:
            pygame.draw.rect(window, self.settings.button_color, button_surf, width=0, 
                border_top_left_radius=8, border_top_right_radius=8, 
                border_bottom_left_radius=8, border_bottom_right_radius=0)

        # text
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, self.aa, self.color)
        text_rect = text.get_rect()
        if self.center:
            text_rect.midleft = (button_surf.midleft[0] + 15, button_surf.midleft[1])

        window.blit(text, text_rect)

