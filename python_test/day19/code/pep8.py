#用实例属性可以操作对象的属性，
class Student:
    def __init__(self, s):
        self.__score = s

    @property
    def score(self):
        '''getter方法'''
        return self.__score

    @score.setter
    def score(self, new_score):
        '''setter方法'''
        assert 0 <= new_score <= 100, "成绩不合法"
        self.__score = new_score


s1 = Student(50)
print(s1.score)
s1.score = 99
print(s1.score)