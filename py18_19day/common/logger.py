"""
============================
author:MuSen
time:2019/5/31
E-mail:3247119728@qq.com
============================
"""
import logging
from py18_19day.common.config import conf


# 读取配置文件中相关数据
logger_name = conf.get('logs', 'logger_name')
level = conf.get('logs', 'level').upper()
sh_level = conf.get('logs', 'sh_level').upper()
fh_level = conf.get('logs', 'fh_level').upper()
log_file_path = conf.get('logs','log_file_path')


class MyLogging(object):
    """自定日志之类"""

    def __new__(cls, *args, **kwargs):
        # 创建自己的日志收集器
        my_log = logging.getLogger(logger_name)
        my_log.setLevel(level)
        # 创建一个日志输出渠道（输出到控制台）
        l_s = logging.StreamHandler()
        l_s.setLevel(sh_level)
        # 创建一个日志输出渠道（输出到文件）
        l_f = logging.FileHandler(log_file_path, encoding='utf8')
        l_f.setLevel(fh_level)
        # 将输出渠道添加到日志收集器中
        my_log.addHandler(l_s)
        my_log.addHandler(l_f)
        # 设置日志输出的格式
        ft = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        ft = logging.Formatter(ft)
        # 设置日志输出的格式
        l_s.setFormatter(ft)
        l_f.setFormatter(ft)
        return my_log


logger = MyLogging()


# if __name__ == '__main__':
    # import os
    # BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    # print(BASE_DIR)