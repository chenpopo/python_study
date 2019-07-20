# enclosure
# 此示例示意封装

class A:
    def __init__(self):
        self.__money = 0
    def show_money(self):
        print("self.__money = ", self.__money)
    def make_money(self, money):
        self.__money += money
        print("self.__money = ", self.__money)

a = A()
a.__money = 100
print(a.__money)

a.show_money()
a.make_money(999)
a.show_money()

