import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

surf = pygame.Surface((200, 100), 0, 32)
surf.fill((50, 50, 50))
s_rect = surf.get_rect()
mx, my = 0, 0
fonts = pygame.font.get_fonts()[:10]

goal = 20*11
scal = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print('down')
                s_rect.move_ip(0, 10)
            if event.key == pygame.K_UP:
                print('up')
                s_rect.move_ip(0, -10)
            if event.key == pygame.K_LEFT:
                print('left')
                s_rect.move_ip(-10, 0)
            if event.key == pygame.K_RIGHT:
                print('right')
                s_rect.move_ip(10, 0)
            if event.key == pygame.K_s:
                surf = pygame.transform.scale(surf, (200, 200))
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                surf = pygame.transform.scale(surf, (200, 100))

        if event.type == pygame.MOUSEMOTION:
            mx, my = pygame.mouse.get_pos()

    if s_rect.collidepoint(mx, my):
        surf.fill((100, 100, 100))

        scal = scal + 5 if scal <= goal else scal
        s_rect = surf.get_rect()
        surf = pygame.transform.smoothscale(surf, (200, scal))
    else:
        surf.fill((50, 50, 50))
        surf = pygame.transform.smoothscale(surf, (200, 100))
        scal = 100

    screen.fill((0, 0, 0))

    for i, f in enumerate(fonts):
        text = pygame.font.SysFont(f, 20).render(f, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (80, 20 * (i +1))
        surf.blit(text, text_rect)

    screen.blit(surf, s_rect)


    pygame.display.flip()