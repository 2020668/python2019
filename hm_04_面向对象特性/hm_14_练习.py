# -*- coding: utf-8 -*-
"""

=================================
@author: keen
Created on: 2019/4/25

E-mail:keen2020@outlook.com

=================================


"""

import  random


class Base(object):
    p = random.randint(1, 10)


class My(Base):
    pass


class Pc(Base):
    pass


my = My()
pc = Pc()
print(my.p)
print(pc.p)
