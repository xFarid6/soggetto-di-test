import pygame


class ToggleButton:
    def __init__(self, x, y, state, size, center=False): 
        self.x = x
        self.y = y
        self.state = state
        self.size = size
        self.center = center

        self.window = pygame.display.get_surface()

        # colors
        self.colors = {
            'sliding': (255, 255, 255),
            'enable': (0, 255, 0), 
            'disable': (255, 0, 0),
        }

        self.underlying_rect = pygame.Rect(self.x - self.size//2, self.y, self.size*1.5, self.size)


    def is_clicked(self, mx, my):
        if self.underlying_rect.collidepoint(mx, my):
            return True


    def draw(self, window=None):
        if window is None:
            window = self.window

        if self.state:
            color = self.colors['enable']
            # draw the rectangle 
            pygame.draw.rect(window, color, self.underlying_rect, 0, 0, 0, 0, 0)

            # draw the left circle
            pygame.draw.circle(window, color, (self.x - self.size//2, self.y + self.size//2), self.size//2, 0)

            # draw the right circle
            pygame.draw.circle(window, color, (self.x + self.size, self.y + self.size//2), self.size//2, 0)

            # draw the sliding circle
            pygame.draw.circle(window, self.colors['sliding'], (self.x + self.size, self.y + self.size//2), self.size//2.2, 0)
        else:
            color = self.colors['disable']
            pygame.draw.rect(window, color, self.underlying_rect, 0, 0, 0, 0, 0)
            pygame.draw.circle(window, color, (self.x - self.size//2, self.y + self.size//2), self.size//2, 0)
            pygame.draw.circle(window, color, (self.x + self.size, self.y + self.size//2), self.size//2, 0)
            pygame.draw.circle(window, self.colors['sliding'], (self.x - self.size//2, self.y + self.size//2), self.size//2.2, 0)