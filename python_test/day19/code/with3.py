class A():
    def __enter__(self):
        print("__enter__方法被调用")
        return self #self 将被 with as 后的变量绑定

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__方法被调用")

        if exc_type is None:
            print("正常离开with语句")
        else:
            print("异常离开with语句")
            print(exc_type, exc_val, exc_tb)

try:
    with A() as a:
        print("这是with内的语句")
        raise ValueError("故意抛出一个错误")
except ValueError:
    print("with 语句内抛出的异常")