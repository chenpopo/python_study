#此示例示意用程序来创建 mynote.txt文件，在向文件中写入一些文字内容，如果文件已经存在，则报错

myfile = open("myfilewritelines.txt", mode="w")
myfile.write("日记\n")
myfile.flush()
myfile.write("world")
myfile.flush()

L = ["北京", "上海","深圳"]
myfile.writelines(L)


myfile.close()

