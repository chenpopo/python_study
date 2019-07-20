import pymysql

db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="db5",
    charset='utf8'
)

# 创建游标对象
cursor = db.cursor()

while True:
    menu = '''
1) 新增成员
2) 退出程序
请做出你的选择:
    '''
    choice = input(menu)
    if choice == '1':
        name = input("请输入姓名: ")
        score = input("请输入成绩: ")

        ins = 'insert into t1(name, score) values(%s, %s)'
        # execute()方法第二个参数，列表传参
        cursor.execute(ins, [name, score])

        db.commit()
        print("%s 传入成功" % name)
    elif choice == '2':
        cursor.close()
        db.close()
        print("成功退出系统")
        break
    else:
        print("无效的选项")