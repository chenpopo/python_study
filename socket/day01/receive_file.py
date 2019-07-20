
from socket import *

f = open("jj.jpg", "wb")

s = socket()
s.bind(("127.0.0.1", 8889))
s.listen(3)

c, addr = s.accept()

while True:
    print("文件接收开始")
    data = c.recv(2014)
    if not data:
        break

    f.write(data)

print("文件接收结束")
f.close()
c.close()
s.close()