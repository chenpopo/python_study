class A:
    def do_work(self):
        print("A")

class B(A):
    def do_work(self):
        print("B")

class C(B):
    def do_work(self):
        print("C")

def work(obj):
    obj.do_work() #请问调用了谁

L = [A(), B(), C(), B()]
for x in L:
    work(x)
