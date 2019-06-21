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

    def __new__(cls, *args, **kwargs):

        my_log = logging.getLogger('py18')
        my_log.setLevel('DEBUG')

        ls = logging.StreamHandler()
        ls.setLevel('INFO')
        my_log.addHandler(ls)

        return my_log


m_log = MyLogging()
m_log.debug('这是debug')
m_log.info('这是info')
