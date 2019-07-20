
def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成4")
    yield 4
    print("即将生成5")
    yield 5
    print("myyield函数调用结束")

gen = myyield() #调用生辰器函数创建一个生成器对象
it = iter(gen)  #从生成器对象gen中拿到迭代器
next(it)
next(it)
next(it)
next(it)
next(it)

print("函数执行结束")



