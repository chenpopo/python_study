
#此示例示意用自定义的生成器函数 myzip 来实现 与zip函数相同的功能
#生成器函数

def myzip(iter1, iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)

    while True:
        try:
            x = next(it1)
            y = next(it2)
            yield (x, y)
        except StopIteration:
            break


numbers = [10086, 10000, 10010, 95588]

names = ["中国移动","中国电信", "中国联通"]

for t in myzip(numbers, names):
    print(t)


for num, name in myzip(numbers, names):
    print(name, "的客服电话是:", num)