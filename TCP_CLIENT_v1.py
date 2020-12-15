#tcp client + "with" statement

import socket
import os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    servaddr = ("127.0.0.1", 1520)
    sock.connect(servaddr)

    # sock.recv, sock.send

    mystr = "hello tcp server"
    sock.sendall(mystr.encode('utf-8'))

    data = sock.recv(64)
    print("server sent:", data.decode('utf-8'))
