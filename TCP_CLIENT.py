#tcp client 

import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servaddr = ("127.0.0.1", 1520)
sock.connect(servaddr)

mystr = "hello tcp server"
sock.send(mystr.encode('utf-8'))

data = sock.recv(64)
print("server sent:", data.decode('utf-8'))

sock.close()