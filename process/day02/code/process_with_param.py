from multiprocessing import Process
from time import sleep

def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" %name)
        print("I'm working")


#p = Process(target=worker, args=(2,"Baron"))
#p = Process(target=worker, kwargs = {'name':"Baron", "sec":2})
p = Process(target=worker, args=(2,),kwargs = {'name':"Baron"})

p.start()
p.join()