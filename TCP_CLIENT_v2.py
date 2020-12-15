#tcp client as a class

import socket
import os

class TcpClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self, addr, port):
        self.addr=addr
        self.port=port
        self.sock.connect((self.addr, self.port))
    
    def mysend(self, mystr):
        self.sock.send(mystr.encode('utf-8'))
        
    def myrecv(self):
        data = self.sock.recv(64)
        return data.decode('utf-8')
        
    def __del__(self):
        self.sock.close()
        
if __name__=="__main__":
    tclient = TcpClient()
    tclient.connect("127.0.0.1", 1600)
    tclient.mysend("Client sent: Hello tcp server!")
    mystr=tclient.myrecv()
    print(mystr)
