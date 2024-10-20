# conda install conda-forge::pygame
import pygame

pygame.init()
W, H = 400, 400
win = pygame.display.set_mode((W, H))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    win.fill((0, 128, 0))
    pygame.display.flip()
