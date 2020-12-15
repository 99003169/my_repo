#tcp server as a class

import socket
import os

class TcpServer:
    def __init__(self, addr, port):
        self.addr=addr
        self.port=port
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind ( (self.addr, self.port) )
        self.sock.listen()
        
    def accept(self):
        (clisock, cliaddr) = self.sock.accept()
        self.clisock = clisock
    
    def mysend(self, mystr):
        self.clisock.send(mystr.encode('utf-8'))
        
    def myrecv(self):
        data = self.clisock.recv(64)
        return data.decode('utf-8')
        
    def __del__(self):
        self.clisock.close()
        self.sock.close()
        
if __name__=="__main__":
    tserver = TcpServer("127.0.0.1", 1600)
    tserver.accept()
    mystr=tserver.myrecv()
    print(mystr)
    tserver.mysend("Server sent: Hi, Thank You")
