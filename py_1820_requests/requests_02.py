# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/11

E-mail:keen2020@outlook.com

=================================


"""

import requests
from requests.sessions import Session

mobilephone = "15071337985"

# 注册
register_url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
data = {"mobilephone": mobilephone, "pwd": "123456", "regname": "baozi"}
response = requests.get(url=register_url, data=data)
html_register = response.content.decode()
print(html_register)

# 创建一个session对象,自动保存上次请求的cookie信息
session = Session()

# 登录
login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
data = {"mobilephone": mobilephone, "pwd": "123456"}
response = session.post(url=login_url, data=data)
html_login = response.content.decode()
print(html_login)
cookie = dict(response.cookies)

# 充值
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
data = {"mobilephone": mobilephone, "amount": 000000}
response = session.post(url=recharge_url, data=data)
html_recharge = response.content.decode()
print(html_recharge)

# 提现
withdraw_url = "http://test.lemonban.com/futureloan/mvc/api/member/withdraw"
data = {"mobilephone": mobilephone, "amount": 000000}
response = session.post(url=withdraw_url, data=data)
html_withdraw = response.content.decode()
print(html_withdraw)

