from random import *


class Test:
    matrix = []


shipsData = [
    [4, 'fourdeck'],
    [3, 'tripledeck'],
    [2, 'doubledeck'],
    [1, 'singledeck']]


def create_matrix():
    arr = []
    for i in range(10):
        arr.append([])
        for j in range(10):
            arr[i].append(0)
    return arr


def random_location():
    Test.matrix = create_matrix()
    for i in range(len(shipsData)):
        decks = shipsData[i][0]
        #print(decks, i)

        for j in range(i + 1):
            coord = get_coordinates(decks)
            # ship = self.testship(coord, decks)
            testship(coord, decks)


def get_random(n):
    return randint(0, n)


def generate_coordinates(decks):
    kx = get_random(1)
    ky = 0 if kx else 1
    x = 0
    y = 0
    if kx:
        x = get_random(10 - decks)
        y = get_random(9)
    else:
        y = get_random(10 - decks)
        x = get_random(9)

    return x, y, kx, ky


def get_coordinates(decks):
    x, y, kx, ky = generate_coordinates(decks)

    #print((x, y, kx, ky, decks))
    while (check_location(x, y, kx, ky, decks)):
        x, y, kx, ky = generate_coordinates(decks)

    #print("return", x, y, kx, ky)
    return x, y, kx, ky


def check_location(x, y, kx, ky, decks):
    from_x = x if x == 0 else x - 1
    to_x = x - kx + decks * kx + 2
    if x == 9 or x - kx + decks * kx == 9:
        to_x -= 1

    from_y = y if y == 0 else y - 1
    to_y = y - ky + decks * ky + 2
    if y == 9 or y - ky + decks * ky == 9:
        to_y -= 1

    #print("square", from_x, from_y, to_x, to_y)
    for i in range(from_x, to_x):
        for j in range(from_y, to_y):
            if Test.matrix[i][j] == 1:
                return True

    return False


def testship(coord, decks):
    x, y, kx, ky = coord
    k = 0
    while k < decks:
        Test.matrix[x + k * kx][y + k * ky] = 1
        k += 1
    # self.__player.set_squadron(self)


def main():
    random_location()
    for i in range(10):
        print(Test.matrix[i])


main()
