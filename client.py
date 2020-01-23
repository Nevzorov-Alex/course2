import sys
import json
import socket
import time
import argparse
import logging

import logs.client_log_config
from decos import log

from common.variables import *
from common.utils import *


# Инициализация клиентского логера
logger = logging.getLogger('client')

# Функция - обработчик сообщений других пользователей, поступающих с сервера.
@log
def message_from_server(message):
    if ACTION in message and message[ACTION] == MESSAGE and SENDER in message and MESSAGE_TEXT in message:
        print(f'Получено сообщение от пользователя {message[SENDER]}:\n{message[MESSAGE_TEXT]}')
        logger.info(f'Получено сообщение от пользователя {message[SENDER]}:\n{message[MESSAGE_TEXT]}')
    else:
        logger.error(f'Получено некорректное сообщение с сервера: {message}')


@log
# Функция запрашивает текст сообщения и возвращает его. Так же завершает работу при вводе подобной комманды
def create_message(sock, account_name='Guest'):
    message = input('Введите сообщение для отправки или \'!!!\' для завершения работы: ')
    if message == '!!!':
        sock.close()
        logger.info('Завершение работы по команде пользователя.')
        print('Спасибо за использование нашего сервиса!')
        exit(0)
    message_dict = {
        ACTION: MESSAGE,
        TIME: time.time(),
        ACCOUNT_NAME: account_name,
        MESSAGE_TEXT: message
    }
    logger.debug(f'Сформирован словарь сообщения: {message_dict}')
    return message_dict



# Функция генерирует запрос о присутствии клиента
@log
def create_presence(account_name='Guest'):
    logger.info(f'Сформировано {PRESENCE} сообщение для пользователя '
                '{account_name}')
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }

    return out


# Функция разбирает ответ сервера
@log
def process_ans(message):
    logger.info(f'Разбор сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        elif message[RESPONSE] == 400:
            return f'400 : {message[ERROR]}'
    raise ValueError

@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-m', '--mode', default='listen', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_mode = namespace.mode

    # проверим подходящий номер порта
    if not 1023 < server_port < 65536:
        logger.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}. Допустимы адреса с 1024 до 65535. Клиент завершается.')
        exit(1)

    # Проверим допустим ли выбранный режим работы клиента
    if client_mode not in ('listen', 'send'):
        logger.critical(f'Указан недопустимый режим работы {client_mode}, допустимые режимы: listen , send')
        exit(1)

    return server_address, server_port, client_mode

def main():
    # Загружаем параметы коммандной строки
    server_address, server_port, client_mode = arg_parser()

    logger.info(f'Запущен клиент с парамертами: адрес сервера: {server_address} , порт: {server_port}, режим работы: {client_mode}')

    # Инициализация сокета и обмен
    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        send_message(transport, create_presence())
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        logger.critical('Did not parse message from server')
        exit(1)
    except ConnectionRefusedError:
        logger.critical(f'Did not connect {server_address}:{server_port}')
        exit(1)
    else:
        # Если соединение с сервером установлено корректно, начинаем обмен с ним, согласно требуемому режиму.
        # основной цикл прогрммы:
        if client_mode == 'send':
            print('Режим работы - отправка сообщений.')
        else:
            print('Режим работы - приём сообщений.')
        while True:
            # режим работы - отправка сообщений
            if client_mode == 'send':
                try:
                    send_message(transport, create_message(transport))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    logger.error(f'Соединение с сервером {server_address} было потеряно.')
                    exit(1)

            # Режим работы приём:
            if client_mode == 'listen':
                try:
                    message_from_server(get_message(transport))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    logger.error(f'Соединение с сервером {server_address} было потеряно.')
                    exit(1)

if __name__ == '__main__':
    main()
