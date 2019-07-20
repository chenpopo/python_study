#此实例示意实例方法的定义语法和调用方法

class Dog:
    def eat(self, food):
        print("ID为", id(self), "的小狗正在吃", food)

    def sleep(self, time):
        print("ID为", id(self), "的小狗睡了", time, "小时")

dog1 = Dog()
dog1.eat("骨头")

dog2 = Dog()
dog2.sleep(3)

#类名.实例方法名(实例，调用传参)
Dog.sleep(dog2, 4)