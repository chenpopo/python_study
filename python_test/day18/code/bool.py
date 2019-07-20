class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __len__(self):
        '''返回0为假，返回非0为真'''
        return len(self.data)

    def __bool__(self):
        return all(self.data)

myl = MyList([0])
print(bool(myl))
if myl:
    print("真")
else:
    print("假")