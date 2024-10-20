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
    [
        pygame.draw.rect(win, (0, 0, 0), (x * 50, y * 50, 50, 50), 1)
        for x in range(8)
        for y in range(8)
    ]
    pygame.display.flip()
