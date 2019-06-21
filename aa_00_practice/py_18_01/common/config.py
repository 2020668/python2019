# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/5

E-mail:keen2020@outlook.com

=================================


"""

import configparser


class ReadConfig(configparser.ConfigParser):

    def __init__(self):

        super().__init__()      # 调用父类__init__方法
        self.read(r'C:\Users\keen\PycharmProjects\python2019\aa_00_practice\py_18_01\conf\config.ini', encoding='utf8')


conf = ReadConfig()
