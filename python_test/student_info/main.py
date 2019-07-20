
'''
思考：
1、当我们这个main.py 文件岁功能的增多， 此文件可能会变得非常庞大，此时要把main.py 拆分成模块
    1） main函数放在 main.py中
    2）show_menu 函数放在menu.py中
    3）与学生操作的函数放在 student_info.py中
2）当用户输入年龄，成绩等信息时，如果输入飞数字的文字，此时会帮亏，如何解决？
    加入异常处理语句，让任何输入都能按逻辑进行

'''

from menu import show_menu
from student_info import *
from infos_file import *

def main():
    L = []

    while True:
        show_menu()
        s = input("请选择：")
        if s == 'q':
            break
        #新增学生信息
        elif s == '1':
            add_student_info(L)
        #显示学生信息
        elif s == '2':
            output_student(L)
        #删除学生信息
        elif s == '3':
            delete_student_info(L)
        #秀爱学生信息
        elif s == '4':
            modify_student_score(L)
        #按照学生成绩高-低降序显示
        elif s == '5':
            output_student_by_score_desc(L)
        #按照学生成绩升序显示
        elif s == '6':
            output_student_by_score_asc(L)
        #按照学生年龄降序显示
        elif s == '7':
            output_student_by_age_desc(L)
        #按照学生年龄升序显示
        elif s == '8':
            output_student_by_age_asc(L)
        #从文件读取数据，初始化学生信息
        elif s == '9':
            L = init_data()
        #将学生成绩保存到文件
        elif s == '10':
            save_data(L)
        elif s == 'q':
            break

main()