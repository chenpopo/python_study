from socket import *
import os, sys
import signal #在父进程中处理僵尸进程


ADDR = ("0.0.0.0", 8888)
FTP_BASH_DIR = "/home/chenpo/ftp_dir/"

class FtpServer(object):
    def __init__(self, c):
        self.c = c
    def do_list(self, path):
        pass
    def do_get(self, filename):
        if os.path.isfile(filename):
            file = open(FTP_BASH_DIR+filename, "r")
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.c.send(data)


        pass
    def do_put(self, filename):
        pass


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
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

        # 处理僵尸进程，设置忽略子进程 向 父进程发送的退出信号。转交给操作系统处理子进程
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        # 创建子进程
        pid = os.fork()
        if pid == 0:  # 创建子进程成功
            # 创建二级子进程，然后把以及子进程关闭，则二级子进程作为孤儿进程，避免出现僵尸进程
            p = os.fork()
            if p == 0:
                s.close()
                ftpserver = FtpServer(c)
                while True:
                    data = c.recv(1024).encode()
                    data = data.split(" ")
                    if not data or data[0] == 'Q':
                        c.close()
                        sys.exit("%s客户端退出"%addr)
                    elif data[0] == 'L':
                        ftpserver.do_list()
                    elif data[0] == 'G':
                        filename = data.split("")[-1]
                        ftpserver.do_get(filename)
                    elif data[0] == 'P':
                        filename = data.split("")[-1]
                        ftpserver.do_put(filename)

            else:
                os._exit(0)
        else:
            c.close()  # 继续接受下一个客户端连接

if __name__ == '__main__':
    main()