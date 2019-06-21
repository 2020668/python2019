# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/26

E-mail:keen2020@outlook.com

=================================


"""

import openpyxl


class ReadExcel(object):
    """
    读取excel数据

    """

    # 打开工作簿
    def __init__(self, file_name, sheet_name):
        """
        初始化读取对象
        :param file_name: 文件名字  --> str
        :param sheet_name: 表单名字  --> str
        """
        # 打开工作簿
        self.wb = openpyxl.load_workbook(file_name)
        self.sheet = self.wb[sheet_name]

    def read_data_line(self):
        """
        按行读取数据
        :return:
        """

        # 按行获取数据并转换成列表
        rows_data = list(self.sheet.rows)

        # 获取表单的表头信息
        titles = []
        for titile in rows_data[0]:
            titles.append(titile.value)
        print(titles)

        # 定义一个列表来存储所有的用例
        cases = []
        for case in rows_data[1:]:
            data = []
            for cell in case:
                if isinstance(cell.value, str):   # 判断是否是字符串
                    data.append(eval(cell.value))
                else:
                    data.append(cell.value)
                data.append(cell.value)
            # print(dict(list(zip(titles, data))))

            # print(data)


    def write_data(self):
        pass


def main():
    r = ReadExcel('cases.xlsx', 'Sheet')
    r.read_data_line()


if __name__ == '__main__':
    main()
