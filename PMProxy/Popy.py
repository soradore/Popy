import SocketHandler

C_PORT = 19133

S_ADDRESS = "localhost"
S_PORT = 8000


class Popy:

    def __init__(self):
        #self.socket = SocketHandler.SocketHandler()
        self.socket = SocketHandler.SocketHandler(C_PORT, S_ADDRESS, S_PORT)
        self.tick()

    def tick(self):
        while True:
            self.socket.tick()


Popy()
