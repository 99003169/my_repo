import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

raddr = ("127.0.0.1", 1800)

mystr = "hello UDP server"
sock.sendto(mystr.encode('utf-8'), raddr)

sock.close()
