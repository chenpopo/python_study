from multiprocessing import Process,Array

shm = Array("i", [1,2,3,4])

def fun():
    for i in shm:
        print(i)
    shm[2] = 1000


p = Process(target = fun)
p.start()
p.join()


for i in shm:
    print(i, end="  ")
print()
print(shm.value)