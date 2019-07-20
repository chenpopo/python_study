#此示例示意 len()函数的重写

class MyList:
    def __init__(self, iterable = ()):
        self.data = [x for x in iterable]

    def __len__(self):
        '''此函数必须只有一个形参self，
        此函数必须返回整数'''
        return len(self.data)

    def __abs__(self):
        L = [abs(x) for x in self.data]
        return MyList(L)    #创建一个新的MyList 对象并返回

    def __repr__(self):
        return 'MyList(%s)' % self.data


myl = MyList([1, -3, 6, 87, 4 -299])
print(len(myl)) #myl.__len__()
print(abs(myl)) #myl.__abs__()
print(myl)      #myl.__repr__()

