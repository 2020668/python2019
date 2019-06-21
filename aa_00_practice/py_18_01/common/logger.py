# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/5

E-mail:keen2020@outlook.com

=================================


"""

import logging
from aa_00_practice.py_18_01.common.config import conf


# 从配置文件获取数据
log_name = conf.get('logs', 'log_name')
level = conf.get('logs', 'level')
sh_level = conf.get('logs', 'sh_level')
fh_level = conf.get('logs', 'fh_level')
log_file_path = conf.get('logs', 'log_file_path')


class MyLogging(object):

    def __new__(cls, *args, **kwargs):

        my_log = logging.getLogger(log_name)
        my_log.setLevel(level)

        ls = logging.StreamHandler()
        ls.setLevel(sh_level)

        lf = logging.FileHandler(log_file_path, encoding='utf8')
        lf.setLevel(fh_level)

        my_log.addHandler(ls)
        my_log.addHandler(lf)

        ft = '%(asctime)s - [%(filename)s -->line:%(lineno)d] - %(levelname)s : %(message)s'
        ft = logging.Formatter(ft)

        ls.setFormatter(ft)
        lf.setFormatter(ft)

        return my_log


my_log = MyLogging()
