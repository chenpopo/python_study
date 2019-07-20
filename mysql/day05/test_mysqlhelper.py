from mysql_helper import MysqlHelper

mysql = MysqlHelper("db5")

name = input("请输入诗人姓名:")
score = input("请输入诗人成绩：")
insert = "insert into t1 values(%s, %s)"
mysql.execute_sql(insert, [name, score])


name = input("请输入要查询的诗人名称:")
sel = "select * from t1 where name=%s"
result = mysql.get_all(sel, [name])
if result:
    print(result[0][0])
else:
    print("无这个诗人")


