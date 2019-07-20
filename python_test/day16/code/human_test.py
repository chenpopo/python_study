class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.skill = []

    def teach(self, other, skill):
        other.skill.append(skill)
        print(self.name, "教", other.name, "学", skill)

    def work(self, money):
        self.money = money
        print(self.name, "上班赚了", money, "元钱")

    def borrow_from(self, other, money):
        self.money = money
        other.money -= money
        print(self.name, "向", other.name, "借了", money, "元")

    def show_info(self):
        print(self.age, "岁的", self.name, "有钱", self.money,
              "元, 他学会的技能是：", ",".join(self.skill))

zhangsan = Human("张三", 30)
lisi = Human("李四", 16)
zhangsan.teach(lisi, "Python")
lisi.teach(zhangsan, "王者荣耀")
zhangsan.work(1000)
lisi.borrow_from(zhangsan, 200)
zhangsan.show_info()
lisi.show_info()
