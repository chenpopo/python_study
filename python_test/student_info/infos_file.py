
def init_data():
    L = []
    try:
        file = open("si.txt")
        while True:
            line = file.readline()
            if not line:
                break
            line = line.strip()
            name, age, score = line.split(",")
            student = dict(name=name, age=int(age), score=int(score))
            L.append(student)
        print("读取文件成功")
    except OSError:
        print("初始化数据失败")
    finally:
        file.close()
    return L


def save_data(L):
    try:
        file = open("si.txt", mode="w")
        for line in L:
            file.write(line["name"] + "," + str(line["age"]) + "," + str(line["score"]) + '\n')
        print("保存数据到文件成功")
    except OSError:
        print("保存数据到文件失败")
    finally:
        file.close()
    return L


if __name__ == "__main__":
    L = init_data()
    print(L)
