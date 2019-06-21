# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/4

E-mail:keen2020@outlook.com

=================================


"""

# import logging
# from py_1819_catelog_frame.common.config import conf
#
#
# # 从配置文件中获取相关数据
#
# log_name = conf.get('logs', 'logger_name')      # 日志收集器名称
# level = conf.get('logs', 'level').upper()     # 收集信息级别，并转换成大写，增加容错机制
# sh_level = conf.get('logs', 'sh_level').upper()     # 输出控制台级别
# fh_level = conf.get('logs', 'fh_level').upper()     # 输出文件级别
# log_file_path = conf.get('logs', 'log_file_path')
#
#
# class MyLogging(object):
#
#     def __new__(cls, *args, **kwargs):
#
#         my_log = logging.getLogger(log_name)        # 创建日志收集器
#         my_log.setLevel(level)      # 设置收集信息级别
#
#         ls = logging.StreamHandler()        # 创建一个日志输出渠道，控制台
#         ls.setLevel(sh_level)       # 设置输出级别
#
#         lf = logging.FileHandler(log_file_path, encoding='utf8')        # 创建日志输出渠道，文件
#         lf.setLevel(fh_level)       # 设置输出级别
#
#         my_log.addHandler(ls)       # 将输出渠道添加到日志收集器中
#         my_log.addHandler(lf)
#
#         # 设置日志输出格式
#         ft = '%(asctime)s - [%(filename)s -->line:%(lineno)d] - %(levelname)s : %(message)s'
#         ft = logging.Formatter(ft)
#
#         # 给输出渠道应用输出格式
#         ls.setFormatter(ft)
#         lf.setFormatter(ft)
#
#         return my_log
#
#
# my_log = MyLogging()


import  logging
from aa_00_practice.py_18_01.common.config import conf


# 从配置文件获取数据
log_name = conf.get('logs', 'log_name')
level = conf.get('logs', 'level')
sh_level = conf.get('logs', 'sh_level')
fh_level = conf.get('logs' 'fh_level')


class MyLogging(object):

    def __new__(cls, *args, **kwargs):

        my_log = logging.getLogger(log_name)
        my_log.setLevel(level)

        ls = logging.StreamHandler()
        ls.setLevel(sh_level)

        lf = logging.FileHandler()
        lf.setLevel(fh_level)

        my_log.addHandler(ls)
        my_log.addHandler(lf)

        ft = '%(asctime)s - [%(filename)s -->line:%(lineno)d] - %(levelname)s : %(message)s'
        ft = logging.Formatter(ft)

        ls.setFormatter(ft)
        lf.setFormatter(ft)

        return my_log


my_log = MyLogging()

