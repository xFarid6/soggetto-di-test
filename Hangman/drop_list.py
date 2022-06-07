import pygame


class DropList: 
    def __init__(self, x, y, options, size, center=False): 
        # init
        self.x = x
        self.y = y
        self.options = options[:10]
        self.size = size
        self.center = center    

        self.selected = None

        # mouse
        self.mx, self.my = 0, 0

        # surface
        self.window = pygame.display.get_surface()
        self.surf = pygame.Surface((min(200, self.size*len(max(options, key=len))), self.size + 5), 0, 32)
        self.s_rect = self.surf.get_rect()
        self.s_rect.topleft = (self.x, self.y)
        self.surf.fill((50, 50, 50))

        # text
        self.text_bb = []
        self.font = pygame.font.SysFont('Arial', self.size)
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.midleft = (10, (i+1)*self.size - self.size/2)
            self.text_bb.append((text, text_rect))

        # surface scaling
        self.goal = self.size * len(self.options)
        self.scale_tracker: int = self.size + 5
        

    def on_click(self, mx, my):
        if self.s_rect.collidepoint(mx, my):
            self.scale_tracker = self.scale_tracker + 3 if self.scale_tracker <= self.goal else self.scale_tracker
            self.surf = pygame.transform.smoothscale(self.surf, (self.s_rect.width, self.scale_tracker))
            self.s_rect = self.surf.get_rect()
            self.s_rect.topleft = (self.x, self.y)


    def restore(self):
        self.scale_tracker = self.scale_tracker - 3 if self.scale_tracker >= self.size + 5 else self.scale_tracker
        self.surf = pygame.transform.smoothscale(self.surf, (self.s_rect.width, self.scale_tracker))
        self.s_rect = self.surf.get_rect()
        self.s_rect.topleft = (self.x, self.y)
        

    def on_hover(self, mx, my):
        if self.s_rect.collidepoint(mx, my):
            self.surf.fill((100, 100, 100))
            return True
        else:
            self.surf.fill((50, 50, 50))
            return False


    def on_select(self, event):
        pass

    def update(self, mx, my):
        self.mx, self.my = mx, my
        for text, text_rect in self.text_bb:
            if text_rect.collidepoint(mx, my):
                self.selected = text
                print(self.selected)


    def draw(self, window=None):
        if window is None:
            window = self.window

        # draw the items
        for text, text_rect in self.text_bb:
            self.surf.blit(text, text_rect)
            if text == self.selected:
                pygame.draw.line(self.surf, 'purple', text_rect.bottomleft, text_rect.bottomright, 2)

        # draw the surface
        window.blit(self.surf, self.s_rect)

        # draw overing rect
        self.on_hover(self.mx, self.my)

        pygame.draw.rect(self.window, (255, 255, 255), self.s_rect, 2)
