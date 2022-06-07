import pygame




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
def draw_text(window, x, y, text, color, size, font):
    font = pygame.font.SysFont(font, size)
    text = font.render(text, True, color)
    window.blit(text, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Hangman")
    pygame.display.flip()
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((255, 255, 255))

        draw_text(window=screen, x=10, y=10, text="Hangman", color=(0, 0, 0), size=30, font="arial")

        pygame.display.flip()
        clock.tick(60)


main()