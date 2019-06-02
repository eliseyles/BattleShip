import pygame
import os
from const import *
from Field import *

pygame.font.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")
drawlist = []
drawlist.append(Field(PLAYER_BOARD, PLAYER_BOARD_COORD, PLAYER_BOARD_START))
drawlist.append(Field(ENEMY_BOARD, ENEMY_BOARD_COORD, ENEMY_BOARD_START))

drawlist[0].random_location()

SHIP_FOUR = pygame.transform.rotate(SHIP_FOUR, 90)


def menu_screen(win):
    run = True

    while run:
        win.fill(WHITE)
        win.blits(BACKS)

        # win.blit(SHIP_FOUR, (66, 99))
        font = pygame.font.SysFont("comicsans", 80)
        title = font.render("Online BattleShip!", 1, (0, 200, 0))
        join = font.render("Click To Join a Game!", 1, (0, 128, 0))
        win.blit(title, (WIDTH / 2 - title.get_width() / 2, 200))
        win.blit(join, (WIDTH / 2 - join.get_width() / 2, 400))
        win_draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False


def win_draw(win):
    for frame in drawlist:
        frame.draw(win)
        for ship in frame.get_squadron():
            ship.draw(win)


menu_screen(win)
