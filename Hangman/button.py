import pygame
from settings_page import SettingsPage

class Button:
    def __init__(self, x, y, text, color, size, font='arial', center=True, aa=True, shadow=True):
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
        button_surf = pygame.Surface((self.width, self.height), 0, 32)
        button_surf.fill(self.color)
        if self.center:
            window.blit(button_surf, (self.x - self.width//2, self.y - self.height//2))
        else:
            window.blit(button_surf, (self.x, self.y))

        # text
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, self.aa, self.color)
        text_rect = text.get_rect()
        if self.center:
            text_rect.center = (self.x, self.y)
        else:
            text_rect.topleft = (self.x, self.y)

        window.blit(text, text_rect)

