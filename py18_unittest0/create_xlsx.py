# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/24

E-mail:keen2020@outlook.com

=================================


"""


import openpyxl

wb = openpyxl.Workbook()
wb.save('cassss.xlsx')
del(wb["sheet1"])

