# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/28

E-mail:keen2020@outlook.com

=================================


"""

import unittest
from py_1816_ExcelClass.py_1816_testcase import RegisterTestCase
from py_1816_ExcelClass.py_1816_readexcel_columns import ReadExcel
from HTMLTestRunnerNew import HTMLTestRunner


suite = unittest.TestSuite()  # 创建测试集合
r = ReadExcel('cases_columns.xlsx', 'Sheet1')
cases = r.read_data([1, 3, 5])   # 调用读取Excel方法，接收测试用例数据，对象的list
for case in cases:  # 取出单个用例对象
    suite.addTest(RegisterTestCase('test_register', case))  # 调用用例对象的方法获取用例数据

with open('report.html', 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='py18_report',
        description='这是我们18期的第一份测试报告',
        tester='keen'
    )
    runner.run(suite)
