# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/16

E-mail:keen2020@outlook.com

=================================


"""


class MobilePhone:
    # 类属性
    call = "打电话"
    texting = "发短信"

    def __init__(self, brand, model, price):
        # 实例属性
        self.brand = brand
        self.model = model
        self.price = price

    def set_clock(self):
        print("闹钟已经设置好了！")

    def show_mobilephone(self):
        print("手机品牌：{}，手机型号：{}，价格：{}" .format(self.brand, self.model, self.price))


# 创建实例对象
iphone7 = MobilePhone("苹果", "iphone7", 5999)
print(iphone7.texting)
iphone7.set_clock()
iphone7.show_mobilephone()
