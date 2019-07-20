#此示例示意用程序来创建 mynote.txt文件，在向文件中写入一些文字内容，如果文件已经存在，则报错

myfile = open("mynote.txt", mode="x")
myfile.write("日记\n")
myfile.write("2019年3月24日 晴")
myfile.close()

