import socket
import time

MAX_SIZE = 64
addr = ("127.0.0.1", 1800)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)
data, addr = sock.recvfrom(MAX_SIZE)
print("Data: ", data, "Address: ", addr)
sock.close()
