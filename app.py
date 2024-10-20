# conda install conda-forge::pygame
import pygame

pygame.init()
W, H = 400, 400
win = pygame.display.set_mode((W, H))
board = [[0] * 8 for _ in range(8)]
board[3][3] = board[4][4] = 1
board[3][4] = board[4][3] = -1
turn = -1

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
    [
        pygame.draw.circle(
            win,
            ((255, 255, 255), (0, 0, 0))[board[y][x] == -1],
            (x * 50 + 25, y * 50 + 25),
            20,
        )
        for y in range(8)
        for x in range(8)
        if board[y][x]
    ]
    pygame.display.flip()
