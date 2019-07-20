from socket import *
s = socket()
s.connect(("127.0.0.1", 8889))

f = open("view.jpg", "rb")
while True:
    print("文件发送开始")
    data = f.read(1024)
    if not data:
        break

    s.send(data)
print("文件发送完毕")
f.close()
s.close()