from random import *
from Ship import *


class Field:
    def __init__(self, sprite, coord, start):
        self.__field_side = 330
        self.__ship_side = 33
        self.__sprite = sprite
        self.__x, self.__y = coord
        self.__start_x, self.__start_y = start
        self.__squadron = []
        self.__startGame = False
        self.__ship_located = False
        self.__shipsData = [
            [4, 'fourdeck'],
            [3, 'tripledeck'],
            [2, 'doubledeck'],
            [1, 'singledeck']]
        self.matrix = []

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

    def create_matrix(self):
        arr = []
        for i in range(10):
            arr.append([])
            for j in range(10):
                arr[i].append(0)
        return arr

    def random_location(self):
        self.clean_field()
        self.matrix = self.create_matrix()
        for i in range(len(self.__shipsData)):
            decks = self.__shipsData[i][0]
            sprite = SHIP[i]

            for j in range(i + 1):
                coord = self.get_coordinates(decks)
                ship = Ship(coord, decks, sprite, self)
                self.set_squadron(ship)
            self.__ship_located = True

    def get_random(self, n):
        return randint(0, n)

    def generate_coordinates(self, decks):
        kx = self.get_random(1)
        ky = 0 if kx else 1
        x = 0
        y = 0
        if kx:
            x = self.get_random(10 - decks)
            y = self.get_random(9)
        else:
            y = self.get_random(10 - decks)
            x = self.get_random(9)

        return x, y, kx, ky

    def get_coordinates(self, decks):
        x, y, kx, ky = self.generate_coordinates(decks)

        while (self.check_location(x, y, kx, ky, decks)):
            x, y, kx, ky = self.generate_coordinates(decks)

        return x, y, kx, ky

    def check_location(self, x, y, kx, ky, decks):
        from_x = x if x == 0 else x - 1
        to_x = x - kx + decks * kx + 2
        if x == 9 or x - kx + decks * kx == 9:
            to_x -= 1

        from_y = y if y == 0 else y - 1
        to_y = y - ky + decks * ky + 2
        if y == 9 or y - ky + decks * ky == 9:
            to_y -= 1

        for i in range(from_x, to_x):
            for j in range(from_y, to_y):
                if self.matrix[i][j] == 1:
                    return True

        return False

    def clean_field(self):
        self.__squadron.clear()
        self.matrix.clear()

    def draw(self, win):
        win.blit(self.__sprite, (self.__x, self.__y))
