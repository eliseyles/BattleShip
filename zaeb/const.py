from pygame import *
import os

font.init()
menu_fonts = font.SysFont("comicsans", 80)
game_fonts = font.SysFont("comicsans", 40)
game_fonts.set_italic(True)
game_fonts.set_underline(True)

WIDTH = 860
HEIGHT = 530
START_POINT = (0, 0)
PATH = "seabattle"
WHITE = (255, 255, 255)

TITLE = menu_fonts.render("Online BattleShip!", 1, (0, 200, 0))
TITLE_COORD = (WIDTH / 2 - TITLE.get_width() / 2, 100)
TITLE_SIZE = TITLE.get_size()

JOIN = menu_fonts.render("Click To Join a Game!", 1, (0, 128, 0))
JOIN_COORD = (WIDTH / 2 - JOIN.get_width() / 2, 300)
JOIN_SIZE = JOIN.get_size()

RANDOM_CHOOSE = game_fonts.render("Random ship location", 1, (102, 67, 210))
RANDOM_CHOOSE_COORD = (WIDTH - RANDOM_CHOOSE.get_width() - 100, 120)
RANDOM_CHOOSE_SIZE = RANDOM_CHOOSE.get_size()

START = menu_fonts.render("Start!", 1, (0, 200, 0))
START_COORD = (WIDTH - START.get_width() - 170, 400)
START_SIZE = START.get_size()

PLAYER_BOARD = transform.scale(image.load(os.path.join(PATH, "bg_play_field.png")), (358, 358))
PLAYER_BOARD_COORD = (42, 73)
PLAYER_BOARD_START = (66, 99)

ENEMY_BOARD = transform.scale(image.load(os.path.join(PATH, "bg_play_field.png")), (358, 358))
ENEMY_BOARD_COORD = (471, 73)
ENEMY_BOARD_START = (495, 99)

SHIP_ONE = image.load(os.path.join(PATH, "1.png"))
SHIP_TWO = image.load(os.path.join(PATH, "2.png"))
SHIP_TREE = image.load(os.path.join(PATH, "3.png"))
SHIP_FOUR = image.load(os.path.join(PATH, "4.png"))

SHIP_ONE.set_colorkey((255, 255, 255))
SHIP_TWO.set_colorkey((255, 255, 255))
SHIP_TREE.set_colorkey((255, 255, 255))
SHIP_FOUR.set_colorkey((255, 255, 255))

SHIP = (SHIP_FOUR, SHIP_TREE, SHIP_TWO, SHIP_ONE)

EMPTY_SHOOT = image.load(os.path.join(PATH, "dot.png"))
DEAD_SHOOT = image.load(os.path.join(PATH, "cross.png"))
NEAR_SHOOT = image.load(os.path.join(PATH, "blue.png"))

EMPTY_SHOOT.set_colorkey((255, 255, 255))
DEAD_SHOOT.set_colorkey((255, 255, 255))
NEAR_SHOOT.set_colorkey((255, 255, 255))

BACK = image.load(os.path.join(PATH, "grid.png"))
BACKS = []
width = START_POINT[0]
height = START_POINT[1]
while width < WIDTH:
    height = START_POINT[1]
    while height < HEIGHT:
        BACKS.append((BACK, (width, height)))
        height += BACK.get_height()
    width += BACK.get_width()
