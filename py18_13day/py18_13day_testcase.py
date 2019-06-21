# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/21

E-mail:keen2020@outlook.com

=================================


"""

import unittest
from py18_13day.login import login_check


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        print("执行每一条测试用例之前，都会使用该方法，做测试前的环境准备")

    # 一个测试用例就是该类中的一个方法

    # 正常登陆验证
    def test_login(self):

        # 预期结果
        excepted = {"code": 0, "msg": "登录成功"}

        # 参数
        data = ("python18", "lemonban")

        # 调用被测的功能函数，传入参数，获取实际结果
        res = login_check(*data)

        try:

            self.assertEqual(excepted, res)
        except AssertionError as e:
            print("该用例测试未通过")
            raise e
        else:
            print("测试通过")

    def test_username_error(self):

        # 预期结果
        excepted = {"code": 1, "msg": "账号或密码不正确"}

        # 参数
        data = ("python", "lemonban")

        # 调用被测的功能函数，传入参数，获取实际结果
        res = login_check(*data)

        try:

            self.assertEqual(excepted, res)
        except AssertionError as e:
            print("该用例测试未通过")
            raise e
        else:
            print("测试通过")

    def test_password_error(self):

        # 预期结果
        excepted = {"code": 1, "msg": "账号或密码不正确"}

        # 参数
        data = ("python18", "lemonban1")

        # 调用被测的功能函数，传入参数，获取实际结果
        res = login_check(*data)

        try:

            self.assertEqual(excepted, res)
        except AssertionError as e:
            print("该用例测试未通过")
            raise e
        else:
            print("测试通过")

    def test_password_gl18(self):

        # 预期结果
        excepted = {"code": 1, "msg": "密码长度必须在6-18位之间"}

        # 参数
        data = ("python18", "lemonbanlemonbanlemonban")

        # 调用被测的功能函数，传入参数，获取实际结果
        res = login_check(*data)

        try:

            self.assertEqual(excepted, res)
        except AssertionError as e:
            print("该用例测试未通过")
            raise e
        else:
            print("测试通过")

    def test_password_fl6(self):

        # 预期结果
        excepted = {"code": 1, "msg": "密码长度必须在6-18位之间"}

        # 参数
        data = ("python18", "lemonban")

        # 调用被测的功能函数，传入参数，获取实际结果
        res = login_check(*data)

        try:

            self.assertEqual(excepted, res)
        except AssertionError as e:
            print("该用例测试未通过")
            raise e
        else:
            print("测试通过")

    def tearDown(self):
        print("每一条用例执行完之后，都会执行该方法，可用来恢复环境")

