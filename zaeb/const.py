import pygame
import os

WIDTH = 860
HEIGHT = 530
START_POINT = (0, 0)
PATH = "seabattle"
WHITE = (255, 255, 255)

PLAYER_BOARD = pygame.transform.scale(pygame.image.load(os.path.join(PATH, "bg_play_field.png")), (358, 358))
PLAYER_BOARD_COORD = (42, 73)
PLAYER_BOARD_START = (66, 99)

ENEMY_BOARD = pygame.transform.scale(pygame.image.load(os.path.join(PATH, "bg_play_field.png")), (358, 358))
ENEMY_BOARD_COORD = (471, 73)
ENEMY_BOARD_START = (495, 99)

SHIP_ONE = pygame.image.load(os.path.join(PATH, "1.png"))
SHIP_TWO = pygame.image.load(os.path.join(PATH, "2.png"))
SHIP_TREE = pygame.image.load(os.path.join(PATH, "3.png"))
SHIP_FOUR = pygame.image.load(os.path.join(PATH, "4.png"))

SHIP_ONE.set_colorkey((255, 255, 255))
SHIP_TWO.set_colorkey((255, 255, 255))
SHIP_TREE.set_colorkey((255, 255, 255))
SHIP_FOUR.set_colorkey((255, 255, 255))

SHIP = (SHIP_FOUR, SHIP_TREE, SHIP_TWO, SHIP_ONE)

EMPTY_SHOOT = pygame.image.load(os.path.join(PATH, "dot.png"))
DEAD_SHOOT = pygame.image.load(os.path.join(PATH, "cross.png"))
NEAR_SHOOT = pygame.image.load(os.path.join(PATH, "blue.png"))

EMPTY_SHOOT.set_colorkey((255, 255, 255))
DEAD_SHOOT.set_colorkey((255, 255, 255))
NEAR_SHOOT.set_colorkey((255, 255, 255))

BACK = pygame.image.load(os.path.join(PATH, "grid.png"))
BACKS = []
width = START_POINT[0]
height = START_POINT[1]
while width < WIDTH:
    height = START_POINT[1]
    while height < HEIGHT:
        BACKS.append((BACK, (width, height)))
        height += BACK.get_height()
    width += BACK.get_width()
