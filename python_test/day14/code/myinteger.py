# 此示例司仪写一个生成器函数， 此生成器函数能够生成从0开始到n结束（不包含n）的一系列整数

def myinteger(n):
    i = 0 #创建i变量，用来绑定生成的数据
    while i < n:
        yield i #生成数据给next(it)函数调用，同时将程序挂起
        i += 1

#for x in myinteger(4):
#    print(x)

# 等同于下面的代码
it = iter(myinteger(4))
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
