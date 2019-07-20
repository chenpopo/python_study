#计算密集
def count(x,y):
    c = 0
    while c< 7000000:
        c += 1
        x += 1
        y += 1


#io密集
def io():
    write()
    read()


def write():
    f = open("test.txt", "w")
    for i in range(1200000):
        f.write("Hello world\n")
    f.close()

def read():
    f = open("test.txt", "r")
    lines = f.readlines()
    f.close()
