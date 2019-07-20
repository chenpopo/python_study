from threading import Thread, Event


s = None
e = Event()
def 杨子荣():
    print("杨子荣前来拜山")
    global s
    s = "天王盖地虎，宝塔镇河妖"
    e.set() #e设置状态为True

t = Thread(target=杨子荣)
t.start()
print("说对口令才是自己人")
e.wait() #等待e被改变状态
if s == "天王盖地虎，宝塔镇河妖":
    print("确认过眼神，你是对的人")
else:
    print("口令错误，打死他")
t.join()