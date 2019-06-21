# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/11

E-mail:keen2020@outlook.com

=================================


"""

import requests


# 发送GET请求 参数：url 请求地址  params:请求的数据，字典类型
register_url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
response = requests.get(url=register_url)

# 获取响应数据
# 获取响应状态码
code = response.status_code

# 获取响应头信息
headers = response.headers

# 获取cookie
cookies = response.cookies

# 获取响应页面内容
# response.text  根据响应头，推测文本编码方式
html = response.text

# response.content  获取字节流数据，进的decode解码
html1 = response.content.decode()    # 默认使用utf8解码

# 指定解码方式
html2 = response.content.decode('utf8')

# 给请求增加参数
data = {"mobilephone": "15071336917", "pwd": "123456", "regname": "laowang"}
# response = requests.get(register_url, params=data)
# html_register = response.content.decode()
# print(html_register)

# 发送POST请求  参数 url:请求地址  data:请求数据,字典类型  json:请求参数json类型
response = requests.post(url=register_url, data=data)
html_register = response.content.decode()
print(html_register)
print(response.request)


