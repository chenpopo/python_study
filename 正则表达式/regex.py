import re

s = "Levi:1994, Sunny:1993"
pattern = r"(\w+):(\d+)"

l = re.findall(pattern, s)
print(l)

regex = re.compile(pattern)
l = regex.findall(s, 0, 12)
print(l)

#切割字符串
s = "hello world how are you L-body"
l = re.split(r"\W+", s)
print(l)


#替换字符串
s = "时间 1942:02:03"
l = re.sub(r"\d+", "00", s, 2 )
print(l)

#返回包含匹配结果的迭代器
s = "2019年，见过70周年"
it = re.finditer(r"\d+", s)
for i in it:
    print(i.group())



s =  """Hello world
你好,中国
"""
#只能匹配ascii字符
regex = re.compile(r"\w+", flags = re.A)
m = regex.findall(s)
print(m)

#忽略字母大小写
regex = re.compile(r"\w+", flags = re.I)
m = regex.findall(s)
print(m)

#.匹配换行
regex = re.compile(r".+", flags = re.S)
m = regex.findall(s)
print(m)


#匹配每一行开头结尾
regex = re.compile(r"^你好", flags = re.M)
m = regex.findall(s)
print(m)



