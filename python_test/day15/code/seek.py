#此示例设置文件的读写位置，实现文件的随机读取

fr = open("20char.txt", "rb")
b =  fr.read(2)
print("当前位置在：", fr.tell())

fr.seek(4, 0)

print("移动后，当前读写位置为：", fr.tell())


b = fr.read(4)
print("b=", b)

fr.close()

