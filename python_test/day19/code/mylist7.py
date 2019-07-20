#此示例示意索引/切片运算符的重载

class MyList:
    def __init__(self, iterable={}):
        self.data = [x for x in iterable]
    def __repr__(self):
        return  "MyList(%s)" % self.data

    def __getitem__(self, item):
        print("__getimte__:", item)
        if type(item) is int:
            print("正在做索引操作, item=", item)
        elif type(item) is slice:
            print("正在做切片操作：")
            print("起始值：", item.start)
            print("终止值：", item.stop)
            print("步长：", item.step)

        return self.data[item]

    def __setitem__(self, key, value):
        print("__setimte()__(key=)", key, ", value=", value)
        self.data[key] = value

    def __delitem__(self, key):
        print("正在删除第", key+1, "个元素")
        del self.data[key]


l1 = MyList([1, -2, 3, -4, 5])
v = l1[::2]   #  ==> v = l1[slice(None, None, 2)]
print(v)