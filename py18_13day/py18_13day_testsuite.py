# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/21

E-mail:keen2020@outlook.com

=================================


"""

import unittest
from py18_13day.py18_13day_testcase import LoginTestCase
from py18_13day import py18_13day_testcase


# 创建一个测试集合
suite = unittest.TestSuite()

# 添加测试用例
# 第一种，单个添加，接收的参数是测试用例对象
suite.addTest(LoginTestCase('test_login'))
suite.addTest(LoginTestCase('test_username_error'))
suite.addTest(LoginTestCase('test_password_error'))
suite.addTest(LoginTestCase('test_password_gl18'))
suite.addTest(LoginTestCase('test_password_fl6'))

# 运行测试集合  创建一个 runner 对象
runner = unittest.TextTestRunner()
runner.run(suite)

# 一次添加一个测试用例类
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))


# 通过模块添加
suite.addTest(loader.loadTestsFromModule(py18_13day_testcase))
runner = unittest.TextTestRunner()
runner.run(suite)
