import pymsql

db = pymsql.connect("localhost","root","root")
cursor = db.cursor()
cursor.execute("create database indexdb;")
cursor.execute("use indexdb;")
cursor.execute("create table t1(id int,name char(20));")
n = 1
name="lucy"
while n <= 20:
    cursor.execute("insert into t1 values('%s','%s')" % (n,name+str(n)))
    # n = int(n)
    n += 1

db.commit()
cursor.close()
db.close()