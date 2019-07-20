from select import *
from socket import *


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

p = poll()
fdmap = {s.fileno(): s}

# 注册要监控的事件
p.register(s, POLLIN)

while True:
    events = p.pool()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fd.accept()
            print("Connect from ", addr)
            p.register(c, POLLIN)
            fdmap[c.s.fileno] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data.decode())
            p.register(fdmap[fd], POLLOUT)
        elif event & POLLOUT:
            fdmap[fd].send(b'OK')
            p.register(fdmap[fd], POLLIN | POLLERR)


