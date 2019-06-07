from Field import *


class Game:
    def __init__(self):
        self.players = [Field((0, 0), (0, 0)), Field((0, 0), (0, 0))]
        self.Ready = [False, False]
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0
        self.turn = 0

    # def get_player_move(self, p):
    #     """
    #     :param p: [0,1]
    #     :return: Move
    #     """
    #     return self.moves[p]
    #
    # def play(self, player, move):
    #     self.moves[player] = move
    #     if player == 0:
    #         self.p1Went = True
    #     else:
    #         self.p2Went = True
    #
    # def connected(self):
    #     return self.ready
    #
    # def bothWent(self):
    #     return self.p1Went and self.p2Went
    #
    # def winner(self):
    #
    #     p1 = self.moves[0].upper()[0]
    #     p2 = self.moves[1].upper()[0]
    #
    #     winner = -1
    #     if p1 == "R" and p2 == "S":
    #         winner = 0
    #     elif p1 == "S" and p2 == "R":
    #         winner = 1
    #     elif p1 == "P" and p2 == "R":
    #         winner = 0
    #     elif p1 == "R" and p2 == "P":
    #         winner = 1
    #     elif p1 == "S" and p2 == "P":
    #         winner = 0
    #     elif p1 == "P" and p2 == "S":
    #         winner = 1
    #
    #     return winner
    #
    # def resetWent(self):
    #     self.p1Went = False
    #     self.p2Went = False

    def create_matrix(self):
        arr = []
        for i in range(10):
            arr.append([])
            for j in range(10):
                arr[i].append(0)
        return arr

    def random_location(self, id):
        self.clean_field(id)
        self.players[id].matrix = self.create_matrix()

        for i in range(len(self.players[id].get_ships_data())):
            decks = self.players[id].get_ships_data()[i][0]

            for j in range(i + 1):
                coord = self.get_coordinates(decks, id)
                self.players[id].set_squadron_tup((coord, decks))
                ship = Ship((coord, decks), self.players[id])
                self.players[id].set_squadron(ship)
            # self.__ship_located = True

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

    def get_coordinates(self, decks, id):
        x, y, kx, ky = self.generate_coordinates(decks)

        while (self.check_location(x, y, kx, ky, decks, id)):
            x, y, kx, ky = self.generate_coordinates(decks)

        return x, y, kx, ky

    def check_location(self, x, y, kx, ky, decks, id):
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
                if self.players[id].matrix[i][j] == 1:
                    return True

        return False

    def clean_field(self, id):
        self.players[id].clean_field()

    def create_enemy(self, id):
        self.random_location(id)
        tup = self.players[id].get_squadron_tup().copy()
        # print("enemy", tup)
        self.players[id].random_location(tup)
        # for i in self.players[id].matrix:
        #     print(i)

    def check_attack(self, coord, id):
        if self.turn == id:
            id = 0 if id == 1 else 1

            if self.players[id].matrix[coord[0]][coord[1]] == 1:
                return "shoot"
            else:
                self.change_turn()
                return "empty"

        else:
            return "not"

    def change_turn(self):
        self.turn = 1 if self.turn == 0 else 0
