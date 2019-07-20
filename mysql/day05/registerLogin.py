from mysql_helper import MysqlHelper
from hashlib import sha1
from getpass import getpass
import string

mysql = MysqlHelper("db5")
# 注册
def register():
    while True:
        # 接受用户名
        username = input("请输入注册用户名:")
        flag = 0
        # 依次把用户名中的每个字符遍历出来判断
        # 定义是否包含特殊字符
        all_chars = string.punctuation + string.whitespace
        for char in username:
            if char in all_chars:
                print("用户名不能包含特殊字符")
                flag = 1
                break
        if flag == 1:
            continue

        # 查询此用户是否存在
        users = mysql.get_all("select name from t1 where name=%s", [username])
        if users:
            print("该用户名已被占用")
        else:
            pwd1 = input("请输入密码：")
            pwd2 = input("请再次输入密码:")
            if pwd1 == pwd2:
                s = sha1()
                s.update(pwd1.encode())
                password = s.hexdigest()
                # 把用户信息存入数据库
                ins = "insert into t1(name, password) values(%s, %s)"
                mysql.execute_sql(ins, [username, password])
                print("注册成功")
            else:
                print("两次密码不一致")

def login():
    i = 0
    while True:
        if i >= 3:
            break
        # 接受用户输入的用户名和密码:
        username = input("请输入登录用户名：")
        password = input("请输入登录密码:")

        # 根据用户名查询密码，查看结果是否为空
        l = "select password from t1 where name=%s"
        result = mysql.get_all(l, [username])
        if result:
            s = sha1()
            s.update(password.encode())
            if result[0][0] == s.hexdigest():
                print("登录成功")
            else:
                print("密码错误，登录失败")
                i += 1
                continue
        else:
            print("该用户不存在")
            i += 1
            continue

    print("尝试错误三次，亲请稍后再试")


def main():
    menu = '''
    1)注册
    2)登录
    q)退出
    请输入您的选择:'''
    choice = input(menu)
    if choice.strip() in ('1', '2', 'q'):
        if choice == "1":
            register()
        elif choice == "2":
            login()
        else:
            print("退出")
    else:
        print("请输入合法的选项")

if __name__ == "__main__":
    main()