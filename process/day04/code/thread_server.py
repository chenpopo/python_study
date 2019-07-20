from socket import *
from threading import Thread
import sys

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


def handle(c):
    c.close()
    pass

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt as e:
        s.close()
        sys.exit("客户端连接断开")

    t = Thread(target = handle, args = (c))
    t.setDaemon(True)
    t.start()