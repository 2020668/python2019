# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/24

E-mail:keen2020@outlook.com

=================================


"""

import unittest
from py18_unittest0.py18_register import register


class RegisterTestCaes(unittest.TestCase):

    def __init__(self, methodName, excepted, data):
        self.excepted = excepted
        self.data = data
        super().__init__(methodName)

    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    def test_register(self):
        res = register(*self.data)
        try:
            self.assertEqual(self.excepted, res)
        except AssertionError as e:
            print("测试未通过")
            raise e
        else:
            print("测试通过")
