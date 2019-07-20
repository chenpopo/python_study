#用实例属性可以操作对象的属性，
class Student:
    def __init__(self, s):
        self.__score = s

    def score(self):
        return self.__score

    def set_score(self, new_score):
        assert 0 <= new_score <=100, "成绩不合法"
        self.__score = new_score

    score = property(score)
    score = score.setter(set_score)


s1 = Student(50)
print(s1.score)
s1.score = 99
print(s1.score)