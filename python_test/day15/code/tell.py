
#类似应用场景为播放音乐或视频，显示当前播放位置

fr = open("20char.txt", 'rb')
print("刚开始时读写位置在：", fr.tell())

b = fr.read(2)
print(b)
print("读完两个字节以后，当前的读写位置在：", fr.tell())

fr.close()