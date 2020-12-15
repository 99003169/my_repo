import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

raddr = ("127.0.0.1", 4444)

mystr = "Requesting current date and time."
print("Requesting current date and time from server")
sock.sendto(mystr.encode('utf-8'), raddr)
data, addr = sock.recvfrom(64)
print(data, "By address: ", addr)
sock.close()
