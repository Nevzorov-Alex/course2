import logging

# Порт поумолчанию для сетевого ваимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'
# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG

# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'sender'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'

# словари и сообщения для тестирования
test_dict_send = {
    ACTION: PRESENCE,
    TIME: 111111.111111,
    USER: {
        ACCOUNT_NAME: 'test_Guest'
    }
}

test_dict_recv_ok = {RESPONSE: 200}

test_dict_recv_err = {
    RESPONSE: 400,
    ERROR: 'Bad Request'
}

MESS_GOOD = '200 : OK'
MESS_BAD = '400 : Bad Request'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
