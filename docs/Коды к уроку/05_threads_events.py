import threading

# функция принимает на вход некий параметр, событие, которое ожидают
# и еще одно событие, для которого необходимо установить True
def writer(x, event_for_wait, event_for_set):
    for i in range(10):
        # ожидать событие
        event_for_wait.wait()
        # сбросить флаг события на false
        event_for_wait.clear()
        # выводим параметр
        print(x)
        # устанавливаем флаг True для второго события
        # потоки, которые его ожидают, активизируются
        event_for_set.set()

# определяем объекты-события
# это объекты-наблюдатели
e1 = threading.Event()
e2 = threading.Event()

# определяем потоки
# в каждом потоке запускаем на выполнение ф-цию writer
# args - позиционные аргументы для ф-ции writer
# 0 или 1, как выодимое значение
# e1, e2 - объекты событий
t1 = threading.Thread(target=writer, args=('Я-первый поток', e2, e1))
t2 = threading.Thread(target=writer, args=('Я-второй поток', e1, e2))

# запускаем потоки
t1.start()
t2.start()

# устанавливаем значение True
# потоки, которые этого ждут - пробуждаются
e1.set()
