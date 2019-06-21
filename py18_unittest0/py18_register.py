# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/24

E-mail:keen2020@outlook.com

=================================


"""

users = [{"user": "python", "password": "123456"}]


def register(username, password1, password2):

    for user in users:
        if username == user["user"]:
            return {"code": 0, "msg": "用户名已存在"}
        if password1 != password2:
            return {"code": 0, "msg": "两次密码不一致"}
        if 6 <= len(username) <= 18 and 6 <= len(password1) <= 18:
            return {"code": 1, "msg": "注册成功"}
        else:
            return {"code": 0, "msg": "账号或密码长度请输入6-18位"}
