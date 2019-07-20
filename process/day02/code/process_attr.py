from multiprocessing import Process

def fn():
    print("进程属性")

p = Process(target = fn)

print("进程id ", p.pid)
print("进程名称", p.name)

p.start()
p.join()

