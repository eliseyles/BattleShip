from const import *
import pygame

class Ship:

    def __init__(self, tup, player):
        coord, decks = tup
        self.__x, self.__y, self.__kx, self.__ky = coord
        self.__decks = decks
        self.__sprite = self.set_sprite()
        if self.__kx:
            self.__sprite = pygame.transform.rotate(self.__sprite, 90)
        self.__player = player
        self.create()

    def set_sprite(self):
        return SHIP[self.__decks-1]

    def create(self):
        k = 0
        while (k < self.__decks):
            self.__player.matrix[self.__x + k * self.__kx][self.__y + k * self.__ky] = 1
            k += 1

    def calc_coord(self):
        y = self.__player.get_start_y() + self.__x * self.__player.get_ship_side()
        x = self.__player.get_start_x() + self.__y * self.__player.get_ship_side()
        return x, y

    def draw(self, win):
        x, y = self.calc_coord()

        win.blit(self.__sprite, (x, y))




