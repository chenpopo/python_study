import gevent 
from gevent import monkey 
monkey.patch_all()  #执行脚本插件修改阻塞行为
from socket import *

#创建套接字
def server():
    s = socket()
    s.bind(('0.0.0.0',9999))
    s.listen(10) 
    while True:
        c,addr = s.accept()
        print("Connect from",addr)
        # handle(c) #循环方案
        gevent.spawn(handle,c) #协程方案

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break 
        print(data.decode())
        c.send(b"Receive message")
    c.close()

server()

