# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/26

E-mail:keen2020@outlook.com

=================================


"""


import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from py_1816_ExcelClass.py_1816_testcase import RegisterTestCase
import openpyxl


class ReadExcel(object):
    """
    读取Excel数据
    """

    # 打开工作簿
    def __init__(self, file_name, sheet_name):
        """
        初始化读取对象
        :param file_name: 文件名称 --> str
        :param sheet_name:  表单名称 --> str
        """

        self.wb = openpyxl.load_workbook(file_name)     # 打开工作簿，传入的指定文件名
        self.sheet = self.wb[sheet_name]        # 选取表单，传入的指定表单

    def read_date_line(self):
        """
        执行读取数据
        :return:
        """

        rows_data = list(self.sheet.rows)       # 按行获取数据，并转换成列表

        titles = []     # 获取表单的表头信息
        for title in rows_data[0]:
            titles.append(title.value)
        # print(titles)

        cases = []      # 定义一个列表来存储所有的用例
        for case in rows_data[1:]:      # 获取每一行的数据
            data = []       # 临时存放用例数据
            for cell in case:       # 获取每一行内部的数据,包括编号int，直接eval会报错
                if isinstance(cell.value, str):     # 编号是int,内部数据是 str ,判断
                    data.append(eval(cell.value))       # 将数据转换成对应格式
                else:
                    data.append(cell.value)     # 编号不作转换

            case_data = dict(list(zip(titles, data)))       # 将表头和内部数据打包，一一对应,将全部用例数据转换成字典
            cases.append(case_data)    # 存入列表
        self.wb.close()
        return cases


if __name__ == '__main__':
    case_obj = ReadExcel("cases.xlsx", "Sheet")      # 传入测试用例文件名，表单名，实例化
    case_list = case_obj.read_date_line()       # 调用读取数据方法，返回所有测试用例数据，list
    suite = unittest.TestSuite()        # 创建测试集合
    for case in case_list:      # 遍历用例列表，依次获取单条用例数据，dict
        # 依次执行单个用例
        suite.addTest(RegisterTestCase('test_register', case["excepted"], case["data"]))

    with open('report.html', 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            verbosity=2,
            title='py18_report',
            description='这是我们18期的第一份测试报告',
            tester='keen'
        )
        runner.run(suite)
