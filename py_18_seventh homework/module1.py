# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/9

E-mail:keen2020@outlook.com

=================================


"""


def play_game():

    # 总把数
    count = 0
    # 胜率把数
    player_win = 0

    while True:
        import random
        computer = random.randint(1, 3)
        player = int(input("请输入数字，1剪刀，2石头，3布,0手动退出："))

        # 手动退出游戏
        if player == 0:

            # 判断一次没玩就退出游戏
            if count == 0:
                print("您还没开始游戏!!!")
                break

            print("游戏结束!!!")
            print("玩家玩了:%d把，赢了:%d把，胜率:%.2f%%" % (count, player_win, player_win/count * 100))
            break

        # elif player < 1 or player > 3:
        elif player not in (1, 2, 3):
            print("请输入1-3之间的数字")
            # 增加换行，美化显示效果
            print()
            continue

        # 把数计数
        count += 1

        print("电脑出拳为：%d" % computer)
        if player == computer - 1 or player == computer + 2:
            print("玩家胜利！")

            # 玩家胜利计数
            player_win += 1

        elif player == computer:
            print("平局！")
        else:
            print("电脑胜利")

        print()


play_game()
