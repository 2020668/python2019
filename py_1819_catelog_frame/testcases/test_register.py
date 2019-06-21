# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/21

E-mail:keen2020@outlook.com

=================================


"""


import unittest
from py_1819_catelog_frame.library.ddt import ddt, data
from py_1819_catelog_frame.register import register
from py_1819_catelog_frame.common.read_excel import ReadExcel
from py_1819_catelog_frame.common.logger import my_log   # 可直接导入对象
from py_1819_catelog_frame.common.config import conf


# 从配置文件获取数据
file_name = conf.get('excel', 'file_name')
sheet_name = conf.get('excel', 'sheet_name')
read_column = conf.get('excel', 'read_column')
read_column = eval(read_column)     # 将str转换成list

# 读取excel数据
wb = ReadExcel(file_name, sheet_name)
cases = wb.read_column_obj(read_column)


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
            my_log.exception(e)     # 将异常信息记录到日志
            raise e
        else:
            result = 'PASS'
            my_log.debug("期望结果：%s, 实际结果：%s, 测试通过" % (eval(case.excepted), res))
        finally:
            wb.write_data(row=self.row, column=4, msg=result)
