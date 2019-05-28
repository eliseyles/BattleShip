import pygame
import os

WIDTH = 860
HEIGHT = 530
START_POINT = (0, 0)

PLAYER_BOARD = (366, 363)

WHITE = (255, 255, 255)

PATH = "seabattle"
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
