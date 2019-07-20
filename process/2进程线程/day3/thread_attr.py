from threading import Thread,currentThread 
from time import sleep

def fun():
    sleep(3)
    #获取当前线程对象
    print("执行%s线程"%currentThread().getName())
    print("线程属性测试")

t = Thread(target=fun,name = "Tarena")

#设置ｄａｅｍｏｎ
t.setDaemon(True)
# t.daemon = True

t.start()

#设置　获取　线程名
t.setName("Tedu")
print("Thread name:",t.name)
print("Thread get name:",t.getName())

print("is alive:",t.is_alive()) #线程状态

# t.join()
print("********主线程结束***********")
