# enclosure
# 此示例示意封装

class A:
    def __init__(self):
        self.__money = 0
    def __moneys(self):
        print("私有方法__moneys 被调用")

    def show_money(self):
        self.__moneys() #调用私有方法
        print("__moneys:", self.__moneys())

a = A()
# a.__moneys() #类外不能调用私有方法
a.show_money()