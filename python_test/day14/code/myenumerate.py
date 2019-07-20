

#此示例示意用自定义的myenumerate 来实现 enumerate 的功能

def myenumerate(iterable, start=0):
    it = iter(iterable)
    while True:
        try:
            yield (next(it), start)
            start += 1
        except StopIteration:
            break


names = ["中国移动","中国电信", "中国联通"]

for t in myenumerate(names):
    print(t)


for t in myenumerate(names, 111):
    print(t)
