# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/21

E-mail:keen2020@outlook.com

=================================


"""


import unittest
from ddt import ddt, data
from py_1818_DDT.py_1818_register import register
from py_1818_DDT.py_1818_readexcel import ReadExcel
from py_1818_DDT.logging_py183 import my_log    # 可直接导入对象

wb = ReadExcel('cases_columns.xlsx', 'Sheet1')
cases = wb.read_data([1, 3, 5])


@ddt
class RegisterTestCase(unittest.TestCase):

    @data(*cases)   # 拆包，拆成几个参数
    # 正常注册
    def test_register(self, case):

        self.row = case.case_id + 1
        res = register(*eval(case.data))    # 拆包元组，变成3个参数
        try:
            self.assertEqual(eval(case.excepted), res)
        except AssertionError as e:
            result = 'FAIL'
            # my_log.debug("期望结果：%s, 实际结果：%s, 测试未通过" % (eval(case.excepted), res))
            # my_log.error(e)
            my_log.exception(e)     # 将异常信息记录到日志
            raise e
        else:
            result = 'PASS'
            my_log.debug("期望结果：%s, 实际结果：%s, 测试通过" % (eval(case.excepted), res))
        finally:
            wb.write_data(row=self.row, column=6, msg=result)
