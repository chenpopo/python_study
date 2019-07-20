# multiple_inherit
#此示例示意 多继的语法和用法

class Plane:
    def fly(self, height):
        print("飞机以海拔", height, "米的高度飞行")

class Car:
    def run(self, speed):
        print("汽车以", speed, "km/h的速度行驶")

class PlaneCar(Plane, Car):
    '''PlanCar同时继承自飞机类和汽车类'''
