"""
============================
author:MuSen
time:2019/6/3
E-mail:3247119728@qq.com
============================
"""
import unittest
from ddt import data, ddt
from py18_19day.register import register
from py18_19day.common.read_excel import ReadExcel
from py18_19day.common.logger import logger
from py18_19day.common.config import conf

# 配置文件中读取excel相关数据
file_name = conf.get('excel', 'file_name')
sheet_name = conf.get('excel', 'sheet_name')
read_columns = conf.get('excel', 'read_columns')


# 读取excel中的数据
wb = ReadExcel(file_name, sheet_name)
cases = wb.readline_data_obj(read_columns)


@ddt
class RegisterTestCase(unittest.TestCase):

    def setUp(self) :
        # 测试用例执行之前执行的
        pass

    def tearDown(self):
        # 测试用例执行完之后执行的
        pass

    @data(*cases)
    def test_register(self, case):
        self.row = case.case_id + 1
        res = register(*eval(case.data))
        try:
            self.assertEqual(eval(case.excepted), res)
        except AssertionError as e:
            res = '失败'
            # logger.exception(e)
            logger.error(e)
            raise e
        else:
            res = 'pass'
            logger.info('该条用例的测试结果:{}'.format(res))

        finally:
            # 在excel中会写结果
            wb.write_data(row=self.row, column=4, msg=res)


if __name__ == '__main__':
    unittest.main()
