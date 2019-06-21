# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/21

E-mail:keen2020@outlook.com

=================================


"""


import unittest
from py_1816_ExcelClass.py_1816_register import register
from py_1816_ExcelClass.py_1816_readexcel_columns import ReadExcel

wb = ReadExcel('cases_columns.xlsx', 'Sheet1')


class RegisterTestCase(unittest.TestCase):

    # 初始化预期和实际结果
    def __init__(self, methodName, case_obj):
        self.excepted = eval(case_obj.excepted)
        self.data = eval(case_obj.data)
        self.row = case_obj.case_id + 1

        # 调用父类方法，传入methodName
        super().__init__(methodName)

    def setUp(self):
        print("执行每一条测试用例之前，都会使用该方法，做测试前的环境准备")

    def tearDown(self):
        print("每一条用例执行完之后，都会执行该方法，可用来恢复环境")

    # 正常注册
    def test_register(self):

        res = register(*self.data)
        try:
            self.assertEqual(self.excepted, res)
        except AssertionError as e:
            res = 'FAIL'
            raise e
        else:
            res = 'PASS'
        finally:
            wb.write_data(row=self.row, column=6, msg=res)



























    # # username已存在
    # def test_username_error(self):
    #     excepted = {"code": 0, "msg": "该账户已存在"}
    #     data = ('python18', '123456', '123456')
    #     res = register(*data)
    #     try:
    #         self.assertEqual(excepted, res)
    #     except AssertionError as e:
    #         print("该条测试用例未通过")
    #         raise e
    #     else:
    #         print("测试通过")
    #
    # # 两次密码不一致
    # def test_password_error(self):
    #     excepted = {"code": 0, "msg": "两次密码不一致"}
    #     data = ('python2019', '123456', '1234567')
    #     res = register(*data)
    #     try:
    #         self.assertEqual(excepted, res)
    #     except AssertionError as e:
    #         print("该条测试用例未通过")
    #         raise e
    #     else:
    #         print("测试通过")
    #
    # # 用户名长度小于6位
    # def test_username_fl6(self):
    #     excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
    #     data = ('lemon', '123456', '123456')
    #     res = register(*data)
    #     try:
    #         self.assertEqual(excepted, res)
    #     except AssertionError as e:
    #         print("该条测试用例未通过")
    #         raise e
    #     else:
    #         print("测试通过")
    #
    # # 密码长度大于18位
    # def test_password_gl18(self):
    #     excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
    #     data = ('python18', 'aasdgh1234907678761', 'aasdgh1234907678761')
    #     res = register(*data)
    #     try:
    #         self.assertEqual(excepted, res)
    #     except AssertionError as e:
    #         print("该条测试用例未通过")
    #         raise e
    #     else:
    #         print("测试通过")
