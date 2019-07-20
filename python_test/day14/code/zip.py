
numbers = [10086, 10000, 10010, 95588]

names = ["中国移动","中国电信", "中国联通"]

for t in zip(numbers, names):
    print(t)


for num, name in zip(numbers, names):
    print(name, "的客服电话是:", num)


for t in zip(numbers, names, range(1, 100)):
    print(t)  # ("中国移动", 10086, 1)