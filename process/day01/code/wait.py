import os
from time import sleep

while True:
    sleep(2)
    pid = os.fork()
    if pid < 0:
        print("Create process failed")
    elif pid == 0:
        print("Child PID：", os.getpid())
        os._exit(1)
    else:
        pid, status = os.wait()
        print("pid:", pid)
        print("status:", status)