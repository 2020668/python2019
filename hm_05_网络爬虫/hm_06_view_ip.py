# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/23

E-mail:keen2020@outlook.com

=================================


"""

import requests
url = 'http://icanhazip.com'

proxy = {
    "http": "35.224.248.29:3128",
}

response = requests.get(url, proxies=proxy)
print(response.text)
