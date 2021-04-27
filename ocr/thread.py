import threading
import time

class Thread(object):

    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                           
        thread.start()                                 

    def run(self):
        while True:
            print('Doing something imporant in the background')
            time.sleep(self.interval)


example = Thread()
time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')
