"""
1.	Для всех функций из урока 3 написать тесты с использованием unittest. Они должны
быть оформлены в отдельных скриптах с префиксом test_ в имени файла
"""


import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))

from client import create_presence, process_ans
from common.variables import *
import unittest

class TestClient(unittest.TestCase):

    # test jo correct request
    def test_def_presense(self):
        test = create_presence()
        test[TIME] = 3.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 3.1, USER: {ACCOUNT_NAME: 'Guest'}})

    # test of correct parse of answer 200
    def test_process_ans_200(self):
        test=process_ans(test_dict_recv_ok)
        self.assertEqual(test,MESS_GOOD)

    # test of correct parse of answer 400
    def test_process_ans_400(self):
        test=process_ans(test_dict_recv_err)
        self.assertEqual(test,MESS_BAD)

    # test without response
    def test_no_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
