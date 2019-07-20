from multiprocessing import Process,Pipe 
import os,time 

#创建管道对象
#如果为单项管道fd1　--> recv
#            fd2 --> send
fd1,fd2 = Pipe(False)

def fun(name):
    time.sleep(3)
    #向管道写入内容
    fd2.send([1,2,3,4])

jobs = []
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

for i in range(5):
    #从管道取出消息
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
