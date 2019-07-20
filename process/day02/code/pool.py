from multiprocessing import Process
from multiprocessing import Pool
from time import sleep


def worker(msg):
    sleep(2)
    print(msg)

#创建进程池对象
pool = Pool(2)

for i in range(10):
    msg = "hello %d"%i
    pool.apply_async(func = worker, args=(msg,))

pool.close()
pool.join()
