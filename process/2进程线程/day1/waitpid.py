import os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    sleep(3)
    print("Child %d process exit"%os.getpid())
    os._exit(3)
else:
    #非阻塞等待
    while True:
        p,status = os.waitpid(-1,os.WNOHANG)
        print("child pid:",p)
        print("child exit status:",\
        os.WEXITSTATUS(status))
        if p != 0:
            break 
        sleep(1)
    while True:    
        print("Parent process....")
        sleep(2)