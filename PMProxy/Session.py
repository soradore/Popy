import socket
import random

class Session:

    def __init__(self, hostip, serverip, serverport):
        self.serverip = serverip
        self.serverport = serverport
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Popy⇔サーバー(PMMP、BDS等)をつなぐソケット
        self.server.bind((hostip, random.randint(49152, 65535)))
        self.server.setblocking(True)
        pass

    def send(self, bytes):
        self.server.sendto(bytes, (self.serverip, self.serverport))
        pass

    def receive(self):
        #サーバ側に返答処理を書いてなかったので適当
        #bytes, address = self.server.recvfrom(65535)
        #print(bytes)
        #if bytes != 0:
        #    if address[0] == self.serverip and address[1] == self.serverport:
        #        return bytes
        #return False
        return ("HUEE").encode()
