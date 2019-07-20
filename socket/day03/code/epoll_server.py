from select import *
from socket import *


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

ep = poll()
fdmap = {s.fileno(): s}

# 注册要监控的事件
ep.register(s, EPOLLIN)

while True:
    events = ep.pool()
    print("有IO需要处理:", events)
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fd.accept()
            print("Connect from ", addr)
            ep.register(c, EPOLLIN | EPOLLERR)
            fdmap[c.s.fileno] = c
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                ep.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data.decode())
            ep.unregister(fd)
            ep.register(POLLOUT)
        elif event & POLLOUT:
            fdmap[fd].send(b'OK')
            ep.unregister(POLLOUT)
            ep.register(fd, POLLIN & POLLERR)

