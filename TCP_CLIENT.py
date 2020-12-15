
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servaddr = ("127.0.0.1", 1510)
sock.connect(servaddr)

# sock.recv, sock.send

data = sock.recv(64)
print("client sent:", data.decode('utf-8'))

mystr = "thank you"
sock.sendall(mystr.encode('utf-8'))


sock.close()
