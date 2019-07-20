
#次示例司仪打开myfile.txt文件，读取文件中的内容到内存中

try:
    #1 打开文件
    myfile = open("myfile.txt") #默认使用字符编码 utf-8, 在window环境下读取文件时，会遇到gbk编码的文件出现异常，encoding='gbk'
    print("文件打开成功")

    #2 读写文件
    s = myfile.read()
    print("myfile.txt文件的内容： ", s)
    #3 关闭文件
    myfile.close()
except OSError:
    print("文件打开失败")
