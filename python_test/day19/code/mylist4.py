#此示例示意一元运算符的重载

class MyList:
    def __init__(self, iterable={}):
        self.data = [x for x in iterable]
    def __repr__(self):
        return  "MyList(%s)" % self.data
    def __neg__(self):
        return [-x for x in self.data]

    def __pos__(self):
        return [+x for x in self.data]
    def __invert__(self):
        return [~x for x in self.data]


l1 = MyList([1, -2, 3, -4, 5])
l2 = -l1
print(l2)

l3 = +l1
print(l3)
l4 = ~l1
print(l4)