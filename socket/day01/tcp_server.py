import socket

#流式套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定地址
sockfd.bind(("0.0.0.0", 8888))

#设置监听，支持最多三个客户端同时连接
sockfd.listen(3)

while True:
    #等待客户端建立连接
    print("waiting for connect")
    connfd, addr = sockfd.accept()
    print("connect from ", addr)

    while True:
        #接受1024个字节
        data = connfd.recv(1024)
        print("receive: " + data.decode())

        if data == b"##":
            break
        #发送信息
        msg = input(">>")
        n = connfd.send(msg.encode())

    #关闭连接和套接字
    connfd.close()
sockfd.close()