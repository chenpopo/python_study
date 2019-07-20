#此示例示意砖石继承问题 super()继承顺序是按照 mro 顺序

class A:
    def go(self):
        print("A")
class B(A):
    def go(self):
        print("B")
        super().go() #C
class C(A):
    def go(self):
        print("C")
        super.go() #A
class D(B, C):
    def go(self):
        print("D")
        super().go() #B

d = D()
d.go() #???