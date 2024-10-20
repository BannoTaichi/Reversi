# conda install conda-forge::pygame
import pygame

pygame.init()
W, H = 400, 400
win = pygame.display.set_mode((W, H))
board = [[0] * 8 for _ in range(8)]
board[3][3] = board[4][4] = 1
board[3][4] = board[4][3] = -1
turn = -1


def flip(x, y, dx, dy):
    r = []
    nx, ny = x + dx, y + dy
    while 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] == -turn:
        r.append((nx, ny))
        nx += dx
        ny += dy
    if 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] == turn:
        return r
    return []


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos[0] // 50, e.pos[1] // 50
            if board[y][x] == 0 and any(
                flip(x, y, dx, dy)
                for dx in [-1, 0, 1]
                for dy in [-1, 0, 1]
                if dx != 0 or dy != 0
            ):
                board[y][x] = turn
                for dx, dy in [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                    (-1, -1),
                    (1, 1),
                    (-1, 1),
                    (1, -1),
                ]:
                    for nx, ny in flip(x, y, dx, dy):
                        board[ny][nx] = turn
                turn *= -1
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
