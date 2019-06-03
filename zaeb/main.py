import pygame
import os
from const import *
from Field import *

pygame.font.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")
drawlist = []
blitlist = []
blitlist.append((TITLE, TITLE_COORD, TITLE_SIZE))
blitlist.append((JOIN, JOIN_COORD, JOIN_SIZE))


def menu_screen(win):
    run = True

    while run:

        win_draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == MOUSEBUTTONDOWN:
                drawlist.append(Field(PLAYER_BOARD, PLAYER_BOARD_COORD, PLAYER_BOARD_START))
                blitlist.clear()
                blitlist.append((RANDOM_CHOOSE, RANDOM_CHOOSE_COORD, RANDOM_CHOOSE_SIZE))
                # drawlist.append(Field(ENEMY_BOARD, ENEMY_BOARD_COORD, ENEMY_BOARD_START))
                # drawlist[0].random_location()
                main(win)
                # x, y = event.pos
                # if Rect(TITLE_COORD, TITLE_SIZE).collidepoint(x, y):
                #     print()


def win_draw(win):
    win.fill(WHITE)
    win.blits(BACKS)
    for b in blitlist:
        win.blit(b[0], b[1])
    for frame in drawlist:
        frame.draw(win)
        for ship in frame.get_squadron():
            ship.draw(win)


def main(win):
    run = True

    while run:

        win_draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if Rect(blitlist[0][1], blitlist[0][2]).collidepoint(x, y):
                    drawlist[0].random_location()
                    blitlist.append((START, START_COORD, START_SIZE))
                if Rect(blitlist[1][1], blitlist[1][2]).collidepoint(x, y):
                    print("Start")



menu_screen(win)
