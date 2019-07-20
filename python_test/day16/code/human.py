class Human:
    def set_info(self, name, age, address='不详'):
        self.name = name
        self.age = age
        self.address = address


    def show_info(self):
        '此处显示此人self的信息'
        print(self.name, "今年", self.age, "岁，家住", self.address)

h1 = Human()
h1.set_info("小张", 20, "北京朝阳区")
h2 = Human()
h2.set_info("小李", 10)
h1.show_info()  # 小张今年20岁，家住...
h2.show_info()  # 小李今年10岁，家住不详