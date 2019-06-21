# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/26

E-mail:keen2020@outlook.com

=================================


"""


import unittest
from py_1816_ExcelClass.py_1816_testcase import RegisterTestCase
from HTMLTestRunnerNew import HTMLTestRunner
import openpyxl


class Case:
    pass


class ReadExcel(object):
    """
    读取Excel数据
    """
    def __init__(self, file_name, sheet_name, test_row):
        """
        初始化读取对象
        :param file_name: 文件名，测试用例文件--> str
        :param sheet_name: 表单名--> str
        :param test_row: 用例的指定行--> list
        """
        self.wb = openpyxl.load_workbook(file_name)     # 打开工作簿，传入的指定文件名
        self.sheet = self.wb[sheet_name]    # 选取表单，传入的指定表单
        self.list = test_row

    def read_data(self):
        """
        执行读取数据
        :return:
        """
        titles = []
        for titile in list(self.sheet.rows)[0]:     # 获取第1行数据，即标题
            titles.append(titile.value)

        cases = []      # 存储测试数据对象
        for case in list(self.sheet.rows)[1:]:   # 按行获取数据，第2行开始
            case_obj = Case()   # 创建对象，存储用例数据，然后添加到cases中
            data = []   # 临时存储数据
            for cell in case:   # 遍历每行的数据
                if isinstance(cell.value, str):     # 内部数据是str，按断并转换成对应数据类型
                    data.append(eval(cell.value))
                else:
                    data.append(cell.value)     # case_id是 int ,无需转换
            case_data = list(zip(titles, data))
            for item in case_data:
                setattr(case_obj, item[0], item[1])     # 对象，属性名，属性值
            # print(case_obj.case_id, case_obj.excepted, case_obj.data)
            cases.append(case_obj)
        return cases


if __name__ == '__main__':
    list1 = [1, 3, 5]
    r = ReadExcel("cases.xlsx", "Sheet", list1)
    suite = unittest.TestSuite()  # 创建测试集合
    cases = r.read_data()   # 调用读取Excel方法，接收测试用例数据，对象的list
    for case in cases:  # 取出单个用例对象
        suite.addTest(RegisterTestCase('test_register', case))  # 调用用例对象的方法获取用例数据

    with open('report.html', 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            verbosity=2,
            title='py18_report',
            description='这是我们18期的第一份测试报告',
            tester='keen'
        )
        runner.run(suite)
