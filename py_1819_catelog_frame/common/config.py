# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/4

E-mail:keen2020@outlook.com

=================================


"""

import configparser


class ReadConfig(configparser.ConfigParser):

    def __init__(self):
        super().__init__()      # 调用父类的__init__方法
        # 读取后，就可以使用了conf.get()获取数据了
        self.read(r'C:\Users\keen\PycharmProjects\python2019\py_1819_catelog_frame\conf\config.ini', encoding='utf8')


conf = ReadConfig()
