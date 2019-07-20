from socket import *
from threading import Thread
import sys

#封装了所有的服务器功能
class HttpServer():
    def __init__(self, addr):
        self.address = addr
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.socketfd = socket()
        self.socketfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.socketfd.bind(self.address)
        self.host = self.address[0]
        self.port = self.address[1]

    def serve_forver(self):
        self.socketfd.listen(3)
        print("Listen the port %s"%self.port)
        while True:
            try:
                connfd, addr = self.socketfd.accept()
            except KeyboardInterrupt:
                self.socketfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error: ", e)
                continue

            t = Thread(target=self.handle, args=(connfd,))
            t.setDaemon(True)
            t.start()


    def handle(self, connfd):
        request = connfd.recv(4096)
        if not request:
            return
        requestlines = request.splitlines()
        info = requestlines[0].decode().split(" ")[1]
        if info == "/" or info[-5:] == ".html":
            self.get_html(connfd, info)
        else:
            self.get_data(connfd)
        connfd.close()

    def get_html(self, connfd, info):
        try:
            f = open(info, "r")
        except Exception as e:
            response = "HTTP/1.1 404 Not found\r\n"
            response += "\r\n"
            response += "Sorry... ..."
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"
            response += f.read()
        finally:
            connfd.send(response.encode())

    def get_data(self, connfd):
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        response += "Waiting ... ..."
        connfd.send(response.encode())


def main():
    ADDR = ("0.0.0.0", 8000)
    httpd = HttpServer(ADDR)
    httpd.serve_forver()

if __name__ == "__main__":
    main()