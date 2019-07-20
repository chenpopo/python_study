#此示例示意索引/切片运算符的重载

class MyList:
    def __init__(self, iterable={}):
        self.data = [x for x in iterable]
    def __repr__(self):
        return  "MyList(%s)" % self.data

    def __getitem__(self, i):
        print("__getimte()__索引为", i)
        return self.data[i]

    def __setitem__(self, key, value):
        print("__setimte()__(key=)", key, ", value=", value)
        self.data[key] = value

    def __delitem__(self, key):
        print("正在删除第", key+1, "个元素")
        del self.data[key]


l1 = MyList([1, -2, 3, -4, 5])
v = l1[2]
print(v)
l1[1] = 100
print(l1)

del l1[4]
print(l1)