#用实例属性可以操作对象的属性，
class Student:
    def __init__(self, s):
        self.score = s

    def get_socre(self):
        return self.score

    def set_score(self, new_score):
        assert 0 <= new_score <=100, "成绩不合法"
        self.score = new_score

s1 = Student(50)
print(s1.get_socre())
s1.set_score(99)
print(s1.get_socre())