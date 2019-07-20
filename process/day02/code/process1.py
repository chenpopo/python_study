from multiprocessing import Process
from time import sleep
import os

def f1():
    print("吃饭")
    sleep(3)
    print(os.getppid(), "---", os.getpid())

def f2():
    print("睡觉")
    sleep(2)
    print(os.getppid(), "---", os.getpid())

def f3():
    print("打豆豆")
    sleep(4)
    print(os.getppid(), "---", os.getpid())

things = [f1, f2, f3]
jobs = []
for t in things:
    p = Process(target = t)
    p.start()
    p.join()


for j in jobs:
    j.join()
