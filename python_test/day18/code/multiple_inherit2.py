# multiple_inherit
#此示例示意多继承存在的问题

# 小张写了一个类A
class A:
    def m(self):
        print("A")

#小李写了一个类B
class B:
    def m(self):
        print("B")

#小王感觉小张和小李写的类自己可以用
class AB(A,B):
    pass

ab = AB()
ab.m() #调用谁，由继承列表中先后书序来决定