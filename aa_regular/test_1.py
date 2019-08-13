# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/10

E-mail:keen2020@outlook.com

=================================


"""

import re


test = 'python34534u232..sd'
res = re.match(r'\d+', test)
if res:
    print(res.group())
else:
    print(res)
