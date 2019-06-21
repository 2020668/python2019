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
from py_1816_DDT.py_1816_register import register
from py_1816_DDT.py_1816_readexcel import ReadExcel

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
            res = 'FAIL'
            raise e
        else:
            res = 'PASS'
        finally:
            # wb.write_data(row=self.row, column=6, msg=res)
            wb.write_data(row=self.row, column=6, msg=res)
