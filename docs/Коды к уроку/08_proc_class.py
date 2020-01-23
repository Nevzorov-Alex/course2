
from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print(f"The time is {time.ctime()}")
            time.sleep(self.interval)

if __name__ == "__main__":
    p = ClockProcess(1)
    p.start()
    p.join()