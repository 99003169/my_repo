#tcp client for file transfer

import socket
import os

class TcpClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self, addr, port):
        self.addr=addr
        self.port=port
        self.sock.connect((self.addr, self.port))
    
    def mysend(self):
        f = open("upload.txt", "rb")
        print("Client sent: file opened")
        data = f.read(10)
        while(data):
            self.sock.send(data)
            data = f.read(10)
            print("data senting")
        f.close()
        self.sock.send(b"DONE")
        print("Client sent: file closed")
        
    def myrecv(self):
        data = self.sock.recv(64)
        return data.decode('utf-8')
        
    def __del__(self):
        self.sock.close()
        
if __name__=="__main__":
    tclient = TcpClient()
    tclient.connect("127.0.0.1", 5555)
    tclient.mysend()
    mystr=tclient.myrecv()
    print(mystr)
