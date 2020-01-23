from threading import Thread
import time

class ClockThread(Thread):
    ''' Класс-наследник потока
    '''
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print(f"Текущее время: {time.ctime()}")
            time.sleep(self.interval)

t = ClockThread(2)
t.start()
t.join()

# Помните также, что не-демонические процессы будут автоматически объединены.
# и тогда можно без join()
