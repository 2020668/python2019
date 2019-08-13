# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/23

E-mail:keen2020@outlook.com

=================================


"""

import requests
import ssl


class HtmlDownloader(object):
    # 通过 url + 页码 + 关键词 获取数据
    def get_page(self, baseUrl, page_num, keyword):
        try:
            #
            # param = {"query": keyword, "city": "101200100", "page": page_num}
            param = {"query": keyword, "city": "101010100", "page": page_num}
            # 设置请求头，模拟浏览器访问
            header = {
                'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                'Referer': r'http://www.zhipin.com/job_detail/',
                'Connection': 'keep-alive'
            }

            result = requests.get(baseUrl, params=param, headers=header)

            # print(result.text)

            return result.text

        except Exception as err:
            print(err)
            print("Boss直聘爬取失败")
            return None