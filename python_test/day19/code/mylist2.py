class MyList:
    def __init__(self, iterable={}):
        self.data = [x for x in iterable]
    def __add__(self, lhs):
        temp = lhs.data + self.data
        return MyList(temp)
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __mul__(self, rhs):
        l = rhs * self.data
        return MyList(l)


l1 = MyList(range(1, 4))
l2 = MyList([4, 5, 6, 7])
l3 = l1 + l2
print(l3)
l4 = l2 + l1
print(l4)
l5 = l1 * 2
print(l5)