from socket import *


def handle(connfd):
    print("Request from :", connfd.getpeername())
    request = connfd.recv(4096)
    # 如果客户端断开
    if not request:
        return

    # 获取请求
    request_line = request.splitlines()[0]
    info = request_line.decode().split(" ")[1]
    if info =='/':
        f = open("index.html")
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += f.read()
        f.close()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type: text/html;charset=utf8\r\n"
        response += "\r\n"
        response += "<h2>没找到网页</h2>"

    connfd.send(response.encode())

def main():
    sockfd = socket()

    sockfd.setsockopt()
    s = socket()
    s.bind(("0.0.0.0", 9999))
    s.listen(5)

    while True:
        client, addr = s.accept()
        handle(client)
    s.close()

main()