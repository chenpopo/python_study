from socket import *

sockfd = socket()
sockfd.connect(("127.0.0.1", 8888))

while True:
    msg = input(">>")
    if not msg:
        break
    sockfd.send(msg.encode())

    data = sockfd.recv(1024)

    print("Server:", data.decode())

sockfd.close()


