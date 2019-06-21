# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/2

E-mail:keen2020@outlook.com

=================================


"""

from py_1818_setconf.my_conf import ReadConf

cf = ReadConf('my.conf', 'utf8')   # 创建对象
name, age = cf.read_conf()  # 调用read_conf 方法，接收返回结果
for item in name:   # 获取name
    data = 'lisi'   # 获取lisi的name
    if item.get(data):
        print(item.get(data))

