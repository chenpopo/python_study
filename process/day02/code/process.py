from multiprocessing import Process

#封装一个函数作为进程的执行函数
def fun():
    print("Hello world")




def main():
    #1、创建一个进程
    p = Process(target= fun)
    #2、启动进程
    p.start()
    #3、回收进程
    p.join()

if __name__ == "__main__":
    main()