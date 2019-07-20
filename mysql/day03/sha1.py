from hashlib import md5

pwd = input("请输入密码：")

# 1、创建sha1加密对象
s = md5()
# 2、进行加密，参数一定为bytes数据类型
s.update(pwd.encode())
# 3、获取十六进制加密结果
pwd = s.hexdigest()

print(pwd)