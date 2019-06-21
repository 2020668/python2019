# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/21

E-mail:keen2020@outlook.com

=================================


"""


def login_check(username, password):
    if 6 <= len(password) <= 18:
        if username == "python18" and password == "lemonban":
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}

    else:
        return {"code": 1, "msg": "密码长度必须在6-18位之间"}
