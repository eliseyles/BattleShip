import pygame
import os
from const import *
from Field import *
import sys
from Network import *

pygame.font.init()

global n
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
                run = False
    run = True

    while run:
        try:
            print(connect())

            # break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
            run = False
        except:
            print("Server Offline")

    main(win)


def win_draw(win):
    win.fill(WHITE)
    win.blits(BACKS)
    for b in blitlist:
        win.blit(b[0], b[1])
    for frame in drawlist:
        frame.draw(win)
        for ship in frame.get_squadron():
            ship.draw(win)


def connect():
    global n
    n = Network()
    return n.connect()


def main(win):
    run = True

    while run:

        win_draw(win)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if not drawlist[0].get_state():
                    if Rect(blitlist[0][1], blitlist[0][2]).collidepoint(x, y):
                        drawlist[0].random_location()
                        print(n.send("Random"), True)
                        blitlist.append((START, START_COORD, START_SIZE))
                    if drawlist[0].get_squadron() != []:
                        if Rect(blitlist[1][1], blitlist[1][2]).collidepoint(x, y):
                            print(n.send("Start"), True)
                            blitlist.clear()
                            drawlist.append(Field(ENEMY_BOARD, ENEMY_BOARD_COORD, ENEMY_BOARD_START))
                            drawlist[0].set_state()
                else:

                    if drawlist[0].get_state() and Rect(drawlist[1].get_start(), drawlist[1].get_end()).collidepoint(x,
                                                                                                                     y):
                        print(n.send(drawlist[1].get_attack_coord((x, y)), True))

            if event.type == pygame.QUIT:
                run = False
                n.disconnect()
                pygame.quit()
                sys.exit()


menu_screen(win)
