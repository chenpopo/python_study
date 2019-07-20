from socket import *
import sys, os

argv = sys.argv
if len(sys.argv) < 3:
    print("argv is error")
    sys.exit(0)
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
s = socket(AF_INET, SOCK_DGRAM)

name = ""

def send_msg():
    while True:
        msg = input("发言:")
        s.sendto(msg.encode(), ADDR)
def receive_msg():
    pass

def main():
    while True:
        name = input("请输入姓名：")
        msg = "L " + name
        #发送给服务端
        s.sendto(msg.encode(), ADDR)

        #等待服务器回应
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已加入聊天室")
            break
        else:
            print(data.decode())

    #创建父子进程，在父子进程中各自处理收发业务
    pid = os.fork()
    if pid < 0:
        print("创建进程失败")
    elif pid == 0:
        send_msg()
    else:
        receive_msg()


if __name__ == "__main__":
    main()