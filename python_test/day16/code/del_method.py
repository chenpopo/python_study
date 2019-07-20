#此示例示意析构方法的语法和作用
class Car:
    def __init__(self, info):
        self.info = info
        print("汽车", self.info, "被创建")

    def __del__(self):
        print("汽车", self.info, "被销毁")

car1 = Car("Audi")
print("程序退出")