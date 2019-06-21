# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/13

E-mail:keen2020@outlook.com

=================================


"""

import requests

"""
封装requests类，根据用例中的请求方法，来决定发起什么类型的请求。输出logging日志
"""


class HTTPRequest(object):

    """直接发起不记录cookies信息的请求"""

    def request(self, method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):

        method = method.lower()
        if method == "post":
            # 判断是否使用json来传参（适用于接口项目有使用json传参）
            if json:
                requests.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                requests.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == "get":
            requests.get(url=url, params=params, headers=headers, cookies=cookies)
