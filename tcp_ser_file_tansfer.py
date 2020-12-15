#tcp server for file transfer

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
        f = open("download.txt", "wb")
        print("Server sent: file opened")
        data = self.clisock.recv(10)
        while(data != b"DONE"):
            f.write(data)
            print("data receiving")
            data = self.clisock.recv(10)
        f.close()
        print("Server sent: file closed")
        
    def __del__(self):
        self.clisock.close()
        self.sock.close()
        
if __name__=="__main__":
    tserver = TcpServer("127.0.0.1", 5555)
    tserver.accept()
    tserver.myrecv()
    tserver.mysend("Server sent: Thank You")
