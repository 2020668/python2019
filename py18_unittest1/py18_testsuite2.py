# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/21

E-mail:keen2020@outlook.com

=================================


"""


import unittest
from py18_unittest1.py18_testcase import RegisterTestCase


suite = unittest.TestSuite()

# 添加一个测试用例类
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))

runner = unittest.TextTestRunner()
runner.run(suite)
