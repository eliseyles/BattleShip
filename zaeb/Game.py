from Field import *

class Game:
    def __init__(self, id):
        self.p = Field((0, 0), (0, 0))
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False

    def create_matrix(self):
        arr = []
        for i in range(10):
            arr.append([])
            for j in range(10):
                arr[i].append(0)
        return arr

    def random_location(self):
        self.clean_field()
        self.p.matrix = self.create_matrix()

        for i in range(len(self.p.get_ships_data())):
            decks = self.p.get_ships_data()[i][0]

            for j in range(i + 1):
                coord = self.get_coordinates(decks)
                self.p.set_squadron_tup((coord, decks))
                ship = Ship((coord, decks), self.p)
                self.p.set_squadron(ship)
            #self.__ship_located = True

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
                if self.p.matrix[i][j] == 1:
                    return True

        return False

    def clean_field(self):
        self.p.clean_field()
