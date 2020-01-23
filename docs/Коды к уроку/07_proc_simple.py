import multiprocessing
import time

def clock(interval):
    while True:
        print(f"The time is {time.ctime()}")
        time.sleep(interval)

if __name__ == "__main__":
    p = multiprocessing.Process(target=clock, args=(1, ))
    p.start()
