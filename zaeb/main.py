import pygame
import os
from const import *

pygame.font.init()


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")
print(BACKS)


def menu_screen(win):
    run = True

    while run:
        win.fill(WHITE)
        win.blits(BACKS)
        font = pygame.font.SysFont("comicsans", 80)
        title = font.render("Online BattleShip!", 1, (0, 200, 0))
        join = font.render("Click To Join a Game!", 1, (0, 128, 0))
        win.blit(title, (WIDTH / 2 - title.get_width() / 2, 200))
        win.blit(join, (WIDTH / 2 - join.get_width() / 2, 400))
        win.blit(PLAYER_BOARD, PLAYER_BOARD_START)
        win.blit(ENEMY_BOARD, ENEMY_BOARD_START)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                run = False


menu_screen(win)
