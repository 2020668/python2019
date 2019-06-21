# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/28

E-mail:keen2020@outlook.com

=================================


"""

import unittest
from py_1818_DDT.py_1818_testcase import RegisterTestCase
from HTMLTestRunnerNew import HTMLTestRunner


suite = unittest.TestSuite()  # 创建测试集合
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))

with open('report.html', 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='py18_report',
        description='这是我们18期的第一份测试报告',
        tester='keen'
    )
    runner.run(suite)
