import pygame
import os

WIDTH = 860
HEIGHT = 530
START_POINT = (0, 0)
PATH = "seabattle"


PLAYER_BOARD = pygame.transform.scale(pygame.image.load(os.path.join(PATH, "bg_play_field.png")), (358, 358))
PLAYER_BOARD_START = (42, 73)

ENEMY_BOARD = pygame.transform.scale(pygame.image.load(os.path.join(PATH, "bg_play_field.png")), (358, 358))
ENEMY_BOARD_START = (471, 73)

WHITE = (255, 255, 255)



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


