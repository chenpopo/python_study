from multiprocessing import Semaphore, Process
from time import sleep
import os

#信号量
sem = Semaphore(3)
def fun():
    sem.acquire()
    print("执行事件：", os.getpid())
    sleep(3)
    print("执行完毕", os.getpid())
    sem.release()

jobs = []
for i in range(5):
    p = Process(target=fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value)