# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/23

E-mail:keen2020@outlook.com

=================================


"""


import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from py1813_unittest2.py18_testcase import RegisterTestCase
import openpyxl


# 读取Excel 中的数据
# 第一步，打开工作簿
wb = openpyxl.load_workbook('cases.xlsx')

# 第二步，选取表单
sh = wb['Sheet']

# 按行读取数据，以字典形式存入列表
# case_list = []
# for case in list(sh.rows)[1:]:
#     case_dict = {}
#     # 将case[1].value转换成字典
#     case_dict["excepted"] = eval(case[1].value)
#     case_dict["data"] = eval(case[2].value)
#     case_list.append(case_dict)
#
# wb.close()

# 按行读取数据，以字典形式存入列表
case_list = []
# 按行读取，从第二行开始
for case in list(sh.rows)[1:]:
    # 将case[1].value转换成字典
    case_dict = dict(excepted=eval(case[1].value), data=eval(case[2].value))
    case_list.append(case_dict)

wb.close()

suite = unittest.TestSuite()

for case in case_list:
    suite.addTest(RegisterTestCase('test_register', case["excepted"], case["data"]))

with open('report.html', 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='py18_report',
        description='这是我们18期的第一份测试报告',
        tester='keen'
    )
    runner.run(suite)
