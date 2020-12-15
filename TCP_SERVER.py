#tcp server

import socket
import os
import time

addr = ("127.0.0.1", 1520)  #tuple

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind(addr)
mysock.listen()               #listening mode

time.sleep(5) 

(clisock,addr) = mysock.accept()
print("got a client conn from ", addr)
#for testing, telnet 127.0.0.1.1500


data = clisock.recv(64)
print("client sent:", data.decode('utf-8'))

mystr = "thank you"
clisock.send(mystr.encode('utf-8'))

time.sleep(5) 

clisock.close()
mysock.close()