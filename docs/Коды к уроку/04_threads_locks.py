import threading

protected_resource = 0
unprotected_resource = 0

NUM = 50000
mutex = threading.Lock()

# Потокобезопасный инкремент
def safe_plus():
    global protected_resource
    for i in range(NUM):
        # Ставим блокировку
        mutex.acquire()
        protected_resource += 1
        mutex.release()

# Потокобезопасный декремент
def safe_minus():
    global protected_resource
    for i in range(NUM):
        mutex.acquire()
        protected_resource -= 1
        mutex.release()

# То же, но без блокировки
def risky_plus():
    global unprotected_resource
    for i in range(NUM):
        unprotected_resource += 1

def risky_minus():
    global unprotected_resource
    for i in range(NUM):
        unprotected_resource -= 1

thread1 = threading.Thread(target=safe_plus)
thread2 = threading.Thread(target=safe_minus)
thread3 = threading.Thread(target=risky_plus)
thread4 = threading.Thread(target=risky_minus)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
print(f"Результат при работе с блокировкой {protected_resource}")
print(f"Результат без блокировки {unprotected_resource}")