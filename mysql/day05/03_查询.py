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

# 定义病执行查询语句
sel = "select * from t1"
cursor.execute(sel)

# fetchone() 方法
one = cursor.fetchone()
print(one)
print("*" * 50)

# fetchmany(n) 方法
many = cursor.fetchmany(2)
print(many)
print("*" * 50)

# fetchall()方法
all = cursor.fetchall()
print(all)
print("*" * 50)

print(all[0][1])


# 关闭
cursor.close()
db.close()
