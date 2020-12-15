#tcp server + "with" statement

import socket
import os
import time

addr = ("127.0.0.1", 1520)  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mysock:
    mysock.bind(addr)
    mysock.listen()               #listening mode

    time.sleep(5) 

    (clisock,addr) = mysock.accept()
    with clisock:
        print("got a client conn from ", addr)
        #for testing, telnet 127.0.0.1.1500
        
        data = clisock.recv(64)
        print("client sent:", data.decode('utf-8'))

        mystr = "thank you"
        clisock.sendall(mystr.encode('utf-8'))