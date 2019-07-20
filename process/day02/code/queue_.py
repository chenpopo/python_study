from multiprocessing import  Process,Queue
import os, time
from random import randint

q = Queue(5)

def request():
    for i in range(20):
        print("-------------")
        x = randint(0,100)
        y = randint(0,100)
        q.put((x, y))

def handle():
    while True:
        time.sleep(0.5)
        x, y = q.get()
        print("%d + %d = %d"%(x, y, x+y))

p1 = Process(target = request)
p2 = Process(target = handle)
p1.start()
p2.start()