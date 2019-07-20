#关于学生信息的各种操作方法定义在此处

def add_student_info(L):
    while True:
        try:
            name = input("请输入学生姓名：")
            if name == "" or name == "":
                break
            try:
                age = int(input("请输入学生年龄："))
                score = int(input("请输入学生成绩："))
            except ValueError:
                print("您的输入有错请重新输入")
                continue

            d = dict(name=name, age=age, score=score)
            L.append(d)
        except ValueError:
            break

def output_student(L):
    print("+-----------------------------------------+")
    print("+------姓名------|-----年龄-----|----成绩---+")
    print("+-----------------------------------------+")
    for d in L:
        name_s = d["name"]
        age_s = str(d["age"])
        score_s = str(d["score"])
        print("+" + name_s.center(16) + "|" + age_s.center(13) + "|" + score_s.center(10) + "+")
    print("+-----------------------------------------+")

def delete_student_info(L):
    '''根据姓名删除学生信息'''
    n = input("请输入要删除学生的姓名:")
    for index, d in enumerate(L):
        if n == d["name"]:
            del L[index]
            print("删除成功")
            break
    print("删除失败，没有找到名为%s的学生" % n)

def modify_student_score(L):
    n = input("请输入要修改成的学生的姓名：")
    for d in L:
        if d["name"] == n:
            score = input("请输入" + n + "的新成绩：")
            d["score"] = score

        print("成绩修改成功")
        break


def get_score(d):
    return d["score"]

def output_student_by_score_desc(L):
    '''根据成绩降序显示学生成绩'''
    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)

def output_student_by_score_asc(L):
    '''根据成绩降序显示学生成绩'''
    L2 = sorted(L, key=get_score)
    output_student(L2)

def get_age(d):
    return d["age"]

def output_student_by_age_desc(L):
    '''根据年龄升序显示学生成绩'''
    L2 = sorted(L, key=get_age, reverse=True)
    output_student(L2)
def output_student_by_age_asc(L):
    '''根据年龄降序显示学生成绩'''
    L2 = sorted(L, key=get_age)
    output_student(L2)
