from threading import Thread, currentThread
from time import sleep

#线程函数
def fun():
    print("属性测试")
    print("%s线程结束" %currentThread().getName())

#创建线程的时候通过name参数给线程取自定义名字
t = Thread(target=fun, name = "tarena")
t.setName("Tedu")
print("name:", t.getName())
t.setDaemon(True) #
t.start()

print("is alive:", t.is_alive())
#t.join()