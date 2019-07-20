#此示例示意
class MyNumber:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        return "aaaaaaaaaa"

n1 = MyNumber(100)
print("repr(ni) = ", repr(n1))
print("str(n1)  = ", str(n1))
print(n1)   #内部会调用str(n1)
