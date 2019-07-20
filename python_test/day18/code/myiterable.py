#此示例示意 MyList类型的对象改写为可迭代对象

class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __iter__(self):
        return MyListIterator(self.data)

class MyListIterator:
    def __init__(self, data):
        self.data = data
        self.cur_index = 0
        return self

    def __next__(self):
        if self.cur_index >= len(self.data):
            raise StopIteration #数据迭代结束，需要通知调用者停止迭代
        r = self.data[self.cur_index]
        self.cur_index += 1
        return r

myl = MyList([3,5,93,-5,32,8])

it = iter(myl)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("迭代器")

