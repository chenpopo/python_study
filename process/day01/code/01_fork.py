import os
from time import sleep

a = 1
pid = os.fork()
if pid < 0:
    print("create process failed")
elif pid == 0:
    print("new process PID:", pid)
    print("a = ", a)
else:
    sleep(4)
    print("old process PID:", pid)


print("test over")