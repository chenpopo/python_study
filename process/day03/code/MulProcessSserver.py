from socket import *
import os
import signal #在父进程中处理僵尸进程


ADDR = ("0.0.0.0", 8888)


def handle(c):
    while True:
        msg = c.recv(1024).decode()
        if not msg: #如果客户端发送了空消息，则退出会话
            break

        print(msg)
        c.send("Hello".encode())


s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

print("Listen the port 8888")

while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    #处理僵尸进程，设置忽略子进程 向 父进程发送的退出信号。转交给操作系统处理子进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    #创建子进程
    pid = os.fork()
    if pid == 0: #创建子进程成功，则在子进程中处理客户端交流
        s.close()
        handle(c)
        os._exit(0)
    else:
        c.close() #继续接受下一个客户端连接


