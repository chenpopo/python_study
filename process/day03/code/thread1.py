from threading import Thread
from time import sleep
import os

a = 1
#线程函数
def music():
    global a #此处声明为global,则线程中操作的是进程的变量
    for i in range(5):
        sleep(2)
        print("播放凉凉", os.getpid())
    a = 10000


#创建线程对象,也是附属与当前进程
t = Thread(target=music)
t.start() #启动线程

#进程启动时默认会生成一个线程，称为主线程
for i in range(4):
    sleep(1.5)
    print("想听凉凉", os.getpid())

t.join() #回收线程

print("a = ", a)