# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/23

E-mail:keen2020@outlook.com

=================================


"""

import requests

url = "https://www.baidu.com"
proxies = {"type": "https", "host": "68.232.175.189", "port": 8080}
# proxies = {"https": "https://68.232.175.189:8080"}
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
                  "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
response = requests.get(url=url, proxies=proxies, headers=headers)
print(response.status_code)
print(response.request.headers)
print(response.text)
