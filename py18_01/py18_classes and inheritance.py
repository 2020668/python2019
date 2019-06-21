# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/18

E-mail:keen2020@outlook.com

=================================


"""


import random


class BaseTank(object):

    # 类属性，定义初始值
    def __init__(self):
        self.live = 1
        self.position = random.randint(1, 10)
        self.HP = 1
        self.attck_position = random.randint(1, 10)

    def hit(self, other):
        if self.attck_position == other.position:
            other.HP -= 1
        if other.HP == 0:
            other.live = 0


class MyTank(BaseTank):

    def move(self):
        while True:
            try:
                # 将位置更新为移动的目标位置
                self.position = int(input("请输入要移动的目标位置【1-10】："))

                # 判断输入是否符合业务规范，不符合则抛出异常
                if self.position not in range(1, 11):
                    ex = Exception("请输入1-10之间的整数")
                    raise ex
                else:
                    return self.position

            # 捕获数据类型错误异常
            except ValueError:
                print("请输入整数！")

            # 捕获抛出的异常
            except Exception as res:
                print(res)

    def Bullet_launch(self):
        while True:
            try:
                self.attck_position = int(input("请输入要攻击的目标位置【1-10】："))
                if self.attck_position not in range(1, 11):
                    ex = Exception("请输入1-10之间的整数")
                    raise ex
                else:
                    return self.attck_position

            except ValueError:
                print("请输入整数！")

            except Exception as res:
                print(res)


class PcTank(BaseTank):

    def move(self):
        # 移动后，更新位置
        self.position = random.randint(1, 10)

    def Bullet_launch(self):
        self.attck_position = random.randint(1, 10)


def main():

    my = MyTank()
    pc = PcTank()

    while True:

        # 玩家和电脑先后开火
        my.Bullet_launch()
        pc.Bullet_launch()

        # 判断是否被击中，并输出战况
        my.hit(pc)
        print("玩家开火=>电脑位置%s,玩家攻击位置%s,电脑生命值%s"
              % (pc.position, my.attck_position, pc.HP))

        if pc.live == 0:
            print("游戏结束，玩家胜利！")
            break

        pc.hit(my)
        print("电脑开火=>玩家位置%s,电脑攻击位置%s,玩家生命值%s"
              % (my.position, pc.attck_position, my.HP))

        # 判断存活状态，为0则输出结果，退出游戏
        if my.live == 0:
            print("游戏结束，电脑胜利！")
            break

        my.move()
        pc.move()


if __name__ == '__main__':
    main()
