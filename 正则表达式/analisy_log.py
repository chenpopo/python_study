import re
def aa(device_name):
    f = open("../5正则表达式/1.txt", "r")
    lines = f.readlines()

    content = ""
    for line in lines:
        if not line:
            continue

        s= re.findall(r"^"+device_name, line)
        if not s:
            continue

        ip = re.findall(r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}", line)
        print(ip)

if __name__== '__main__':
    while True:
        device_name = input("请输入设备号：")
        if not device_name:
            print("设备号不允许为空!")
            continue
        break;

    aa(device_name)