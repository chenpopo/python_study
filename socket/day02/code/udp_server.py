from socket import *


sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(("0.0.0.0", 8888))

def find_word(word):
    f = open("../dict.txt", "r")
    for line in f:
        tmp = line.split(" ")[0]
        if tmp == word:
            f.close()
            return line
    f.close()
    return "Not found"

# 收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    print("Receive:", data.decode())
    mean = find_word(data.decode())
    sockfd.sendto(mean.encode(), addr)


# 关闭套接字
sockfd.close()



