import pymysql

db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="db5",
    charset='utf8'
)
cursor = db.cursor()
insert = "insert into t1 values(5, '苏轼', 91)"
upd = "update t1 set score=100 where id=1"
delete = "delete from t1 where id=5"
try:
    cursor.execute(insert)
    cursor.execute(upd)
    cursor.execute(delete)
    db.commit()
    print("OK")
except Exception as e:
    print("Error", e)
    db.rollback()

cursor.close()
db.close()

