"""
============================
author:MuSen
time:2019/6/3
E-mail:3247119728@qq.com
============================
"""
import configparser

"""
为什么要封装？
    封装是为了使用起来更加方便，
    
封装的需求？
    封装成什么样子才能达到我们的目的
    
封装的原则：
    写死的固定数据(变量)，可以封装成类属性
    实现某个功能的代码封装成方法
    在各个方法中都要用到的数据，抽离出来作为实例属性
    
"""


# 封装前读使用，读取数据
# conf = configparser.ConfigParser()
# conf.read('config.ini',encoding='utf8')
# conf.get('excel','file_name')


class ReadConfig(configparser.ConfigParser):

    def __init__(self):
        # 实例化对象
        super().__init__()
        # 加载文件
        self.read(r'C:\Users\keen\PycharmProjects\python2019\py18_19day\conf\config.ini', encoding='utf8')


conf = ReadConfig()

