# 1,有四个数字：1、2、3、4，
# 能组成多少个互不相同且无重复数字的三位数？
# 各是多少？
# 123
# 124
# 132
# 134
# 142
# 143
# a = 0
# x = 1
# while x <= 4:  #控制百位
#     y = 1
#     while y <=4:  #控制十位
#         i = 1
#         while i <= 4: #控制个位
#             if x != y and y != i and x != i:
#                 a += 1
#                 print(x, y, i)
#             i += 1
#         y += 1
#     x += 1
# print(a)

# a= 0
# for x in range(1,5):
#     for y in range(1,5):
#         for i in range(1,5):
#             if x != y and y!= i and x!=i:
#                 a += 1
#                 print(x,y,i)
# print(a)








# 6，输入三个整数x,y,z，
# 请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，
# 先将x与y进行比较，
# 如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，
# 如果x>z则将x与z的值进行交换，
# 这样能使x最小。

l = []
for i in range(3):
    x = int(input("输入数: "))
    l.append(x)
l.sort()
print(l)



