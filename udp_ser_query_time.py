import socket
import datetime

addr = ("127.0.0.1", 4444)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr)
data, addr = sock.recvfrom(64)
print(data, "By address: ", addr)
mystr = str(datetime.datetime.now())
sock.sendto(mystr.encode('utf-8'), addr)
sock.close()