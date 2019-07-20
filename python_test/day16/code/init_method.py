#此示例示意初始化方法的定于语法和用法

class Car:
    '''此类为小汽车类'''
    def __init__(self, c, b, m):
        self.color = c
        self.brand = b
        self.model = m
        print("Car类的__init__被调用")

    def run(self, speed):
        print(self.color, "的", self.brand, self.model, "正在以", speed, "公里/小时的速度行驶")


c1 = Car("红色", "Audi", "A6L")
c1.run(299)


c1 = Car("白色", "BYD", "秦EV Pro")
c1.run(199)