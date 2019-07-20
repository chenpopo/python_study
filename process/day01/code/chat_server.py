from socket import *
import os, sys


# 用于接收各种客户端请求，调用相应的函数处理
# 格式{"zhangsan":("127.0.0.1", 8888)}
user = {}

ADDR = ("0.0.0.0", 8888)
s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDR)

def do_login(name, address):
    if user[name] != None:
        s.send_to(name + " 已经加入了聊天室".encode(), address)
        return

    # 先往每个客户端发送欢迎通知
    do_chat("欢迎 "+name+" 加入聊天室", name)
    #再将新用户加入用户列表
    user[name] = address

#群发聊天内容
def do_chat(name, msg):
    msg = "%s 说： %s"%(name,msg)
    for u in user:
        if u != name:
            s.send_to(msg.encode(), user[u])

#用户退出聊天室
def do_quit(name):
    msg = "\n%s退出了聊天室"%name
    for u in user:
        if u == name:
            s.sendto(b"EXIT", user[u])
        else:
            s.sendto(msg.encode(), user[u])
    #从聊天室队列中删除当前用户
    del user[name]

def do_request():
    while True:
        msg, address = s.recvfrom(1024)
        msgList = msg.decode().split(" ")

        #接收到的登录请求，格式"L xxxxx"
        if msgList[0] == "L":
            do_login(msgList[1], address)

        #发送聊天消息，格式"C name xxxxx"
        elif msgList[0] == "C":
            # 重新组织消息
            msg = ' '.join(msgList[2:])
            do_chat(msgList[1], msg)
        #退出聊天室，格式"Q name"
        elif msgList[0] == "Q":
            do_quit(msgList[1], address)

def main():
    do_request()

    pid = os.fork()
    if pid < 0:
        print("创建子进程失败")
    elif pid == 0: #子进程处理管理员发言，再调用父进程
        msg = input("管理员消息: ")
        msg = "C 管理员 %s"%msg
        do_chat("管理员", msg)
    else:
        do_request()


if __name__ == "__main__":
    main()