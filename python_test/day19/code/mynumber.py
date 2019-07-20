class MyNumber:
    def __init__(self, value):
        self.data = value
    def __repr__(self):
        return "MyNumber(%d)" % self.data
    def __add__(self, other):
        temp = self.data + other.data
        return MyNumber(temp)
    def __sub__(self, other):
        temp = self.data - other.data
        return MyNumber(temp)



n1 = MyNumber(100)
n2 = MyNumber(200)
#n3 = n1.__add__(n2)
n3 = n1 + n2
print(n3)

n4 = n1 - n2
print(n4)