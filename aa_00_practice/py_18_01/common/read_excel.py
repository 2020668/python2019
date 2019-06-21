# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/6/5

E-mail:keen2020@outlook.com

=================================


"""

import openpyxl


class ReadExcel(object):

    """
    读取Excel数据
    """
    def __init__(self, file_name, sheet_name):

        """
        :param file_name:
        :param sheet_name:
        """
        self.wb = openpyxl.load_workbook(file_name)
        self.sheet = self.wb[sheet_name]
        self.file_name = file_name

    def __del__(self):
        self.wb.close()

    def read_line(self):






