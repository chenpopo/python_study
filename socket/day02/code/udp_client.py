from socket import *

s = socket(AF_INET, SOCK_DGRAM)

ADDR = ("127.0.0.1", 8888)

while True:
    data = input("Msg>>")
    if not data:
        break
    s.sendto(data.encode(), ADDR)
    msg, addr = s.recvfrom(1024)
    print(msg.decode())

s.close()