#此实例示意属性的创建和使用
class Dog:
    def eat(self, food):
        print(self.color, "的", self.kinds, "正在吃", food)

dog1 = Dog()
dog1.kinds = "哈士奇"
dog1.color = "黑白色"
dog2 = Dog()
dog2.kinds = "京巴"
dog2.color = "白色"

dog1.eat("骨头")
dog2.eat("狗粮")