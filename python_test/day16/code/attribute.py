#此实例示意属性的创建和使用
class Dog:
    pass

dog1 = Dog()
dog1.kinds = "哈士奇"
dog1.color = "黑白色"
print(dog1.color, "的", dog1.kinds)


dog1.color='黄色'
print(dog1.color, "的", dog1.kinds)

dog2 = Dog()
dog2.kinds = "京巴"
dog2.color = "白色"
print(dog2.color, "的", dog2.kinds)