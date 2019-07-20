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

name = input("请输入学生姓名：")
sel = 'select * from t1 where name=%s'
cursor.execute(sel, [name])

result = cursor.fetchone()[2]
print("%s 的成绩是 %s" % (name, result))

cursor.close()
db.close()
