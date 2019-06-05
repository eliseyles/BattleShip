import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5555
        self.addr = (self.host, self.port)

    def connect(self):
        self.client.connect(self.addr)
        data = self.send("start")
        return data

    def disconnect(self):
        # self.send("close")
        self.client.close()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            print(data)
            self.client.send(pickle.dumps(data))
            reply = self.client.recv(1024)
            try:
                reply = pickle.loads(reply)
            except Exception as e:
                print(e)

            return reply
        except socket.error as e:
            print(e)
