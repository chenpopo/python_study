import gevent
from gevent import Timeout
 
timeout = Timeout(2)  # 2 seconds
timeout.start()
 
def wait():
    gevent.sleep(10)
 
try:
    gevent.spawn(wait).join()
except Timeout:
    print('Could not complete')