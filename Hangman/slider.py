import pygame


class Slider:
    def __init__(self, x, y, lenght, radius, min_max, center=False): 
        self.x = x
        self.y = y
        self.lenght = lenght
        self.radius = radius
        self.range = min_max
        self.center = center
        self.value = 0

        self.bar_color_active = (200, 170, 200)
        self.bar_color_inactive = (80, 80, 80)
        self.circle_color = (255, 255, 255)


    def update(self, mx, my):
        pass


    def draw(self):
        # draw bar active

        # draw bar inactive

        # draw circle

        pass
        