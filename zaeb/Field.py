from random import *
from Ship import *


class Field:
    def __init__(self, coord, start):
        self.__field_side = 330
        self.__ship_side = 33
        self.__sprite = self.set_sprite()
        self.__shoot = DEAD_SHOOT
        self.__empty = EMPTY_SHOOT
        self.__x, self.__y = coord
        self.__start_x, self.__start_y = start
        self.__squadron = []
        self.__sq_tuple = []
        self.__startGame = False
        # self.__ship_located = False
        self.__shipsData = [
            [4, 'fourdeck'],
            [3, 'tripledeck'],
            [2, 'doubledeck'],
            [1, 'singledeck']]
        self.matrix = self.create_matrix()
        self.__end = (self.__start_x + self.__field_side, self.__start_y + self.__field_side)

    def set_sprite(self):
        return BOARD

    def get_state(self):
        return self.__startGame

    def get_ships_data(self):
        return self.__shipsData

    def set_state(self):
        self.__startGame = True

    def set_squadron_tup_full(self, data):
        # self.__sq_tuple.clear()
        self.__sq_tuple = data
        # print('client1', self.get_squadron_tup())

    def set_squadron_tup(self, data):
        self.__sq_tuple.append(data)

    def get_squadron_tup(self):
        return self.__sq_tuple

    def set_squadron(self, ship):
        self.__squadron.append(ship)

    def get_squadron(self):
        return self.__squadron

    def get_ship_side(self):
        return self.__ship_side

    def get_start_x(self):
        return self.__start_x

    def get_start_y(self):
        return self.__start_y

    def get_start(self):
        return (self.__start_x, self.__start_y)

    def get_end(self):
        return self.__end

    def create_matrix(self):
        arr = []
        for i in range(10):
            arr.append([])
            for j in range(10):
                arr[i].append(0)
        return arr

    def random_location(self, tup):
        self.clean_field()
        # print('client1', tup)
        self.set_squadron_tup_full(tup)
        self.matrix = self.create_matrix()
        # print('client2', self.get_squadron_tup())
        # for i in range(len(self.__shipsData)):
        #     decks = self.__shipsData[i][0]
        #
        #     for j in range(i + 1):
        #         coord = self.get_coordinates(decks)
        #         self.set_squadron_tup((coord, decks))
        #         ship = Ship((coord, decks), self)
        #         self.set_squadron(ship)
        # self.__ship_located = True
        for i in range(len(self.get_squadron_tup())):
            # print(self.get_squadron_tup()[i])
            ship = Ship(self.get_squadron_tup()[i], self)
            self.set_squadron(ship)

    # def get_random(self, n):
    #     return randint(0, n)
    #
    # def generate_coordinates(self, decks):
    #     kx = self.get_random(1)
    #     ky = 0 if kx else 1
    #     x = 0
    #     y = 0
    #     if kx:
    #         x = self.get_random(10 - decks)
    #         y = self.get_random(9)
    #     else:
    #         y = self.get_random(10 - decks)
    #         x = self.get_random(9)
    #
    #     return x, y, kx, ky
    #
    # def get_coordinates(self, decks):
    #     x, y, kx, ky = self.generate_coordinates(decks)
    #
    #     while (self.check_location(x, y, kx, ky, decks)):
    #         x, y, kx, ky = self.generate_coordinates(decks)
    #
    #     return x, y, kx, ky
    #
    # def check_location(self, x, y, kx, ky, decks):
    #     from_x = x if x == 0 else x - 1
    #     to_x = x - kx + decks * kx + 2
    #     if x == 9 or x - kx + decks * kx == 9:
    #         to_x -= 1
    #
    #     from_y = y if y == 0 else y - 1
    #     to_y = y - ky + decks * ky + 2
    #     if y == 9 or y - ky + decks * ky == 9:
    #         to_y -= 1
    #
    #     for i in range(from_x, to_x):
    #         for j in range(from_y, to_y):
    #             if self.matrix[i][j] == 1:
    #                 return True
    #
    #     return False

    def clean_field(self):
        self.__squadron.clear()
        self.matrix = self.create_matrix()
        self.__sq_tuple.clear()

    def draw(self, win):
        win.blit(self.__sprite, (self.__x, self.__y))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 2:
                    win.blit(self.__shoot, self.get_blit_coord(i, j))
                if self.matrix[i][j] == -1:
                    win.blit(self.__empty, self.get_blit_coord(i, j))

    def get_blit_coord(self, i, j):
        return (self.get_start_x() + self.get_ship_side() * j, self.get_start_y() + self.get_ship_side() * i)

    def get_attack_coord(self, coord):
        x, y = coord
        return ((y - self.get_start_y()) // self.get_ship_side(), (x - self.get_start_x()) // self.get_ship_side())
