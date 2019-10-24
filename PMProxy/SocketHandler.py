import socket
import Session

class SocketHandler:

    def __init__(self):
        import Popy

        self.popyip = socket.gethostname()
        self.popyport = Popy.C_PORT

        self.serverip = Popy.S_ADDRESS
        self.serverport = Popy.S_PORT

        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#クライアント(MCBE)⇔Popy間をつなぐソケット
        self.client.bind((self.popyip, self.popyport))
        self.client.setblocking(False)

        self.sessions = {}


    def tick(self):
        try:
            self.serverSocket()
            self.clientSocket()
        except socket.error:
            pass


    def clientSocket(self):
        bytes, address = self.client.recvfrom(65535)
        if bytes != 0:
            key = address[0] + ":" + str(address[1])
            if key not in self.sessions:
                print(key + "からデータが送られてきました")
                self.sessions[key] = Session.Session(self.popyip, self.serverip, self.serverport)
            self.sessions[key].send(bytes)

    def serverSocket(self):
        for key in self.sessions:
            bytes = self.sessions[key].receive()
            if bytes != 0:
                address = key.split(":")
                self.client.sendto(bytes, (address[0], address[1]))
            pass