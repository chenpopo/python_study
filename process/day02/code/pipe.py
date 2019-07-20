from multiprocessing import Pipe, Process
import time, os

#创建管道
fd1, fd2 = Pipe()

def fun(name):
    time.sleep(3)
    fd1.send({name:os.getpid()}) #向管道写入内容

jobs = []
for i in range(5):
    p = Process(target = fun, args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = fd2.recv()  #读取管道
    print(data)