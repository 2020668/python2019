# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/30

E-mail:keen2020@outlook.com

=================================


"""

import logging


class MyLogging(object):

    # new方法，创建并返回一个对象，重写new方法
    def __new__(cls, *args, **kwargs):

        # 创建自己的日志收集器
        my_log = logging.getLogger('py18')
        my_log.setLevel('DEBUG')

        # my_log.debug('这是我的debug')
        # my_log.info('这是我的info')

        # 创建一个日志输出渠道，控制台
        ls = logging.StreamHandler()
        ls.setLevel('INFO')

        # 创建一个日志输出渠道，文件
        lf = logging.FileHandler('login.log', encoding='utf8')
        lf.setLevel('DEBUG')

        # 将输出渠道添加到日志收集器中
        my_log.addHandler(ls)
        my_log.addHandler(lf)

        # 设置日志输出格式
        ft = '%(asctime)s - [%(filename)s -->line:%(lineno)d] - %(levelname)s : %(message)s'
        ft = logging.Formatter(ft)

        ls.setFormatter(ft)
        lf.setFormatter(ft)

        return my_log


my_log = MyLogging()    # 创建对象会触发new方法

my_log.debug('这是我的debug')
my_log.info('这是我的info')
my_log.warning('这是我的warning')
my_log.error('这是我的error')
my_log.critical('这是我的critical')



