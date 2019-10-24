import SocketHandler

C_PORT = 19133

S_ADDRESS = "localhost"
S_PORT = 19132


class Popy:

    def __init__(self):
        self.socket = SocketHandler.SocketHandler()
        self.tick()

    def tick(self):
        while True:
            self.socket.tick()


Popy()