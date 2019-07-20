from socket import *
from select import *

s = socket()
s.bind(("", 8888))
s.listen(3)  #创建套接字后会有一个IO, 下面rlist监听这个IO

rlist = [s] #s作为套接字进行监听. 如果有客户端连接进来则将连接也放在列表中
wlist = []
xlist = []

rs, ws, xs = select(rlist, wlist, xlist)

while True:
    for r in rs:
        #rs中每个元素，如果是socket则检测是否有新的连接；如果是连接，则检测是否有消息发送过来
        if r is s:
            c, addr = r.accept()
            print("connect from ", addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            # 当前客户端退出后，则结束本次IO
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            c.send(b'OK')
