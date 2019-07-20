import pymysql

class MysqlHelper(object):
    # 初始化数据库连接参数
    def __init__(self, database, host='127.0.0.1', user='root', password='root', charset='utf8'):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset

    # 打开数据库连接
    def open(self):
        self.db = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset
        )
        self.cursor = self.db.cursor()

    # 关闭数据库连接
    def close(self):
        self.cursor.close()
        self.db.close()

    # 执行sql语句
    def execute_sql(self, sql, l=[]):
        self.open()
        self.cursor.execute(sql, l)
        self.db.commit()
        self.close()

    #
    def get_all(self, sql, l=[]):
        self.open()
        self.cursor.execute(sql, l)
        result = self.cursor.fetchall()
        self.close()
        return result


if __name__ == "__main__":
    mysql = MysqlHelper("db5")