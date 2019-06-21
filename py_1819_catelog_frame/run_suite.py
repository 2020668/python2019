# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/4

E-mail:keen2020@outlook.com

=================================


"""

import unittest
from py_1819_catelog_frame.library.HTMLTestRunnerNew import HTMLTestRunner
from py_1819_catelog_frame.common.config import conf


_title = conf.get('report', 'title')
_description = conf.get('report', 'description')
_tester = conf.get('report', 'tester')
report_file_path = conf.get('report', 'report_file_path')


suite = unittest.TestSuite()  # 创建测试集合
loader = unittest.TestLoader()
suite.addTest(loader.discover(r'C:\Users\keen\PycharmProjects\python2019\py_1819_catelog_frame\testcases'))

with open(report_file_path, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title=_title,
        description=_description,
        tester=_tester
    )
    runner.run(suite)
