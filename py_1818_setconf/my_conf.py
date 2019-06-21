# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/2

E-mail:keen2020@outlook.com

=================================


"""


import configparser


class ReadConf(object):

    def __init__(self, filename, method):

        self.filename = filename
        self.method = method

    def read_conf(self):

        conf = configparser.ConfigParser()      # 创建ConfigParser对象
        cf = conf.read(self.filename, encoding=self.method)     # 读取打开配置文件

        name = []   # 将section -- > name 的内容存入单独的一个列表
        name_data = conf.items('name')
        for i in name_data:
            data_dict = {i[0]: i[1]}
            name.append(data_dict)

        age = []    # 将section -- > age 的内容存入单独的一个列表
        age_data = conf.items('age')
        for i in age_data:
            data_dict = {i[0]: i[1]}
            age.append(data_dict)

        return name, age



