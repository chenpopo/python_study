#此示例示意 in , not in 运算符的重载

class MyList:
    def __init__(self, iterable={}):
        self.data = [x for x in iterable]
    def __repr__(self):
        return  "MyList(%s)" % self.data
    def __contains__(self, item):
        return item in self.data


l1 = MyList([1, -2, 3, -4, 5])
if 3 in l1:
    print("真")
else:
    print("假")