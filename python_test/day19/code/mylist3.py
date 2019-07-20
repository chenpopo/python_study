class MyList:
    def __init__(self, iterable={}):
        self.data = [x for x in iterable]
    def __repr__(self):
        return  "MyList(%s)" % self.data
    def __add__(self, rhs):
        print("__add__方法被调用")
        temp = self.data + rhs.data
        return MyList(temp)
    def __iadd__(self, rhs):
        print("__iadd__方法被调用")
        # L = self.data + rhs.data
        # return MyList(L)
        self.data += rhs.data
        return self


l1 = MyList(range(1, 4))
l2 = MyList([4, 5, 6, 7])
print("+=之前的id:", id(l1))
l1 += l2
print(l1)
print("+=之后的id:", id(l1))