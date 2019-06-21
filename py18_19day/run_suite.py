"""
============================
author:MuSen
time:2019/6/3
E-mail:3247119728@qq.com
============================
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner


# 创建一个测试集合
suite = unittest.TestSuite()


# 创建loader对象
loader = unittest.TestLoader()


# 添加测试用例
suite.addTest(loader.discover(r'C:\Users\keen\PycharmProjects\python2019\py18_19day\testcases'))


# 执行测试用例生成测试报告
with open('reports/reports.html', 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='py18_report',
        description='这是我们18期的第一份测试报告',
        tester='MuSen')
    runner.run(suite)

