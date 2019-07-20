#此示例 用二进制方式写文件
#此文件包含256个字节，第一个字节的值为0， 第二个字节的值为1...最后一个字节的值为255

#打开文件
fw = open("bin256.txt", "wb")

b = bytes(range(256))
print(b)
count = fw.write(b)
print("成功写入字节串", count, "个字节")

fw.close()