from threading import Thread
from time import sleep

def fun(sec,name):
    print("多线程参数传递")
    sleep(sec)
    print("%s 线程结束"%name)

thread = []
for i in range(3):
    t = Thread(target=fun, args = [2,1])
    thread.append(t)
    t.start()

for i in thread:
    i.join()
    print("2222")