#用实例属性可以操作对象的属性，
class Student:
    def __init__(self, s):
        self.score = s

s1 = Student(50)
print(s1.score)
s1.score=999
print(s1.socre)