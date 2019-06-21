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
# register_url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
# data = {"mobilephone": mobilephone, "pwd": "123456", "regname": "baozi"}
# response = requests.post(url=register_url, data=data)
# html_register = response.content.decode()
# print(html_register)


# 登录
# login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
# data = {"mobilephone": mobilephone, "pwd": "123456"}
# response = requests.post(url=login_url, data=data)
# html_login = response.content.decode()
# print(html_login)
# print(dict(response.cookies))

# headers 请求头，dict类型，可传入User-Agent,cookies,Content-Type先登录一次，复制其中的cookies值，然后关闭登录请求，只执行充值，将使用该cookies值，即可成功执行充值
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "cookie": "JSESSIONID= 87B74FF851B650B1C471AAA85EB6B8D0"
}

# 充值
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
data = {"mobilephone": mobilephone, "amount": 000000}
response = requests.post(url=recharge_url, data=data, headers=headers)
html_recharge = response.content.decode()
print(html_recharge)

# 提现
withdraw_url = "http://test.lemonban.com/futureloan/mvc/api/member/withdraw"
data = {"mobilephone": mobilephone, "amount": 000000}
response = requests.post(url=withdraw_url, data=data, headers=headers)
html_withdraw = response.content.decode()
print(html_withdraw)
