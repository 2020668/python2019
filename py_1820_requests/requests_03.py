# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/13

E-mail:keen2020@outlook.com

=================================


"""

import requests

mobilephone = "15071337986"

# 注册
register_url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
data = {"mobilephone": mobilephone, "pwd": "123456", "regname": "baozi"}
response = requests.post(url=register_url, data=data)
html_register = response.content.decode()
print(html_register)


# 登录
login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
data = {"mobilephone": mobilephone, "pwd": "123456"}
response = requests.post(url=login_url, data=data)
html_login = response.content.decode()
print(html_login)

# 可将登录后的cookie提取出来，加入后续请求内
cookie = response.cookies

# 充值
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
data = {"mobilephone": mobilephone, "amount": 000000}
response = requests.post(url=recharge_url, data=data, cookies=cookie)
html_recharge = response.content.decode()
print(html_recharge)

# 提现
withdraw_url = "http://test.lemonban.com/futureloan/mvc/api/member/withdraw"
data = {"mobilephone": mobilephone, "amount": 000000}
response = requests.post(url=withdraw_url, data=data, cookies=cookie)
html_withdraw = response.content.decode()
print(html_withdraw)
