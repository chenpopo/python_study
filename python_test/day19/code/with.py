#此示例示意with语句的用法

try:
    file = open("../day19.txt")
    try:
        line1 = file.readline()

        print("第一行内容是：", line1)
        n = int(line1)  #
        print(n)
    finally:
        file.close()
        print("文件已关闭")
except OSError:
    print("文件打开失败")
except ValueError:
    print("读写文件出错")