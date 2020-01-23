# ======================= Потоки и многозадачность ============================
# ---------------- Обзор возможностей модуля multiprocessing ------------------

#         Синхронизация процессов через неименованные каналы Pipe

import multiprocessing
import time

# Получает элементы из канала.
def consumer(pipe):
    output_p, input_p = pipe
    input_p.close()         # Закрыть конец канала, доступный для записи
    while True:
        try:
            item = output_p.recv()
        except EOFError:
            break
        # Обработать элемент
        print('извлекаю')
        print(item)         # Замените эту инструкцию фактической обработкой
        time.sleep(2)
    # Завершение
    print("Потребитель завершил работу")


# Создает элементы и помещает их в канал. Переменная sequence представляет
# итерируемый объект с элементами, которые требуется обработать.
def producer(sequence, input_p):
    for item in sequence:
        print('отправляю')
        # Послать элемент в канал
        input_p.send(item)
        time.sleep(2)


if __name__ == '__main__':
    # output_p, input_p - кортеж (концы канала)
    output_p, input_p = multiprocessing.Pipe()
    # Запустить процесс-потребитель
    cons_p = multiprocessing.Process(target=consumer, args=((output_p, input_p), ))
    cons_p.start()

    # Закрыть в поставщике конец канала, доступный для чтения
    output_p.close()

    # Отправить элементы
    sequence = [1, 2, 3,4]
    producer(sequence, input_p)

    # Сообщить об окончании, закрыв конец канала, доступный для записи
    input_p.close()

    # Дождаться, пока завершится процесс-потребитель
    cons_p.join()
