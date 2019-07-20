#此示例示意with语句的用法

try:
    with open("../day19.txt") as file:
        line1 = file.readline()
        print("第一行内容是：", line1)
        n = int(line1)
        print(n)
except OSError:
    print("文件打开失败")
except ValueError:
    print("读写文件出错")