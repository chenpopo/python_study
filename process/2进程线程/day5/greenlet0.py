from greenlet import greenlet 

def test1():
    print(12)
    gr2.switch() #去执行协成２
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

#将两个函数变为协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()  #执行协成test1