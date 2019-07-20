from threading import Thread
from time import *

class MyThread(Thread):
    #重写父类的run方法
    def run(self):
        tm = time()
        self._target(*self._args, **self._kwargs)
        print(time() - tm)

def player(song, sec):
    for i in range(2):
        print("Playing %s: %s"%(song, ctime()))
        sleep(sec)

t = MyThread(target=player, args=("凉凉",3))
t.start()
t.join()