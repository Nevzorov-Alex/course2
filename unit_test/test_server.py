"""
1.	Для всех функций из урока 3 написать тесты с использованием unittest. Они должны
быть оформлены в отдельных скриптах с префиксом test_ в имени файла
"""


import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))

from server import process_client_message
from common.variables import *
import unittest


class TestServer(unittest.TestCase):

    # no action
    def test_action_no(self):
        self.assertEqual(process_client_message({TIME : '1.1' ,
             USER : {ACCOUNT_NAME : 'Guest'}}), test_dict_recv_err)

    # bad action
    def test_action_bad(self):
        self.assertEqual(process_client_message({ACTION: 'Wrong',
            TIME : '1.1' , USER : {ACCOUNT_NAME : 'Guest'}}), test_dict_recv_err)

    # no time
    def test_action_no_time(self):
        self.assertEqual(process_client_message({ACTION:PRESENCE ,
            USER : {ACCOUNT_NAME : 'Guest'}}), test_dict_recv_err)

    # no accaunt
    def test_action_no_accaunt(self):
        self.assertEqual(process_client_message({ACTION:PRESENCE ,
            TIME : '1.1' }), test_dict_recv_err)

    # no GAST
    def test_action_no_gast(self):
        self.assertEqual(process_client_message({ACTION:PRESENCE ,
            TIME : '1.1' , USER : {ACCOUNT_NAME : 'Guest6'}}), test_dict_recv_err)

    # test without error
    def test_action_ok(self):
        self.assertEqual(process_client_message({ACTION:PRESENCE ,
            TIME : '1.1' , USER : {ACCOUNT_NAME : 'Guest'}}), test_dict_recv_ok)

if __name__ == '__main__':
    unittest.main()

