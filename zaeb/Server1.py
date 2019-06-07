import socket
from _thread import *
import pickle
import time
from Game import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ""
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

game = Game()
connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    # conn.send(str.encode(str(p)))
    # print(conn)

    while True:
        try:
            data = conn.recv(2048)
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    # # print(datetime.datetime.now(), conn)
                    # if data == "reset":
                    #     game.resetWent()
                    # elif data != "get":
                    #     game.play(p, data)
                    # reply = pickle.dumps(game)
                    # print(sys.getsizeof(reply))
                    # conn.sendall(pickle.dumps(game))
                    data = pickle.loads(data)
                    print("receive from ", addr, data)
                    if data[0] == "Random":
                        game.random_location(p)
                        conn.send(pickle.dumps(game.players[p].get_squadron_tup()))
                    elif data[0] == "Start":
                        # game.(data[1])
                        conn.send(pickle.dumps("ok"))
                    elif data[0] == "Attack":
                        conn.send(pickle.dumps(game.check_attack(data[1], p)))
                    else:
                        conn.send(pickle.dumps("ok"))
                    print("send to ", addr)


            else:
                break
        except:
            break

    print("Lost connection")

    try:
        del games[gameId]
        print("Closing Game", gameId)

    except:
        pass

    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game()
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))

# import socket
# import sys
# from _thread import *
# import pickle
# from game import Game
# import datetime
#
# server = "127.0.0.1"
# port = 5555
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.bind((server, port))
# except socket.error as e:
#     str(e)
#
# s.listen(2)
# print("Waiting for a connection, Server Started")
#
# connected = set()
# games = {}
# idCount = 0
#
#
# def threaded_client(conn, p, gameId):
#     global idCount
#     conn.send(str.encode(str(p)))
#     # print(conn)
#
#     reply = ""
#     while True:
#         try:
#             data = conn.recv(4096).decode()
#
#             if gameId in games:
#                 game = games[gameId]
#
#                 if not data:
#                     break
#                 else:
#                     #print(datetime.datetime.now(), conn)
#                     if data == "reset":
#                         game.resetWent()
#                     elif data != "get":
#                         game.play(p, data)
#                     reply = pickle.dumps(game)
#                     print(sys.getsizeof(reply))
#                     conn.sendall(pickle.dumps(game))
#             else:
#                 break
#         except:
#             break
#
#     print("Lost connection")
#
#     try:
#         del games[gameId]
#         print("Closing Game", gameId)
#
#     except:
#         pass
#     idCount -= 1
#     conn.close()
#
#
# while True:
#     conn, addr = s.accept()
#     print("Connected to:", addr)
#
#     idCount += 1
#     p = 0
#     gameId = (idCount - 1) // 2
#     if idCount % 2 == 1:
#         games[gameId] = Game(gameId)
#         print("Creating a new game...")
#     else:
#         games[gameId].ready = True
#         p = 1
#
#     start_new_thread(threaded_client, (conn, p, gameId))
