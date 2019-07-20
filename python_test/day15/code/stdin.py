
import sys

s = sys.stdin.readline()#读取第一行
print("刚才读取", len(s), "个字符")
print("内容是：", s)

sys.stdin.close() #关闭标准输入文件，则会引起 input异常

s2 = input("请输入文字：")  #内部就是使用sys.stdin.readline() 来实现的