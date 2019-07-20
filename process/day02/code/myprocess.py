from multiprocessing import Process


class Clock(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()

    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    def run(self):
        print(self.value)
        self.f1()
        self.f2()


p = Clock(2)
p.start()
p.join()
