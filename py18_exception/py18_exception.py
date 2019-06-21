# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/14

E-mail:keen2020@outlook.com

=================================


"""


# 第3题，有个程序，运行起来会提醒用户输入文件名，然后打开（r模式打开）读取内容，打印出来
# 不存在打开文件会报错，请用捕获改异常，让用户重新输入，
# def read_data():
#     while True:
#         file_name = input("请输入文件名：")
#         try:
#             with open(file_name, "r", encoding="utf8") as file:
#                 print("成功打开文件，读取内容如下：")
#                 print(file.read())
#                 print()
#         except FileNotFoundError:
#             print("文件不存在，请重新输入文件名，注意文件后缀！")
#             print()
#
#
# read_data()


# 第4题，改进剪刀石头布
def play_game():

    # 总把数
    count = 0
    # 玩家胜把数
    player_win = 0
    try:
        with open("game.txt", encoding="utf8") as file:
            sum_record = eval(file.read())
        sum_count = sum_record["count"]
        sum_player_win = sum_record["player_win"]
        print("历史战绩：总场数{},玩家胜利{},玩家胜率{:.2%}". format(sum_count, sum_player_win, sum_player_win/sum_count))
        print()
    # 对历史战绩文件不存在或文件为空的异常处理
    except (FileNotFoundError, ZeroDivisionError, SyntaxError):
        print("历史战绩记录不存在！")
        print()
        sum_count = 0
        sum_player_win = 0

    while True:
        with open("game.txt", "w", encoding="utf8") as file:
            import random
            computer = random.randint(1, 3)
            try:
                player = int(input("请输入数字，1剪刀，2石头，3布,0手动退出："))
                # 对输入输在不是1,2,3,0进行提示
                if player not in (1, 2, 3, 0):
                    ex = Exception("输入非法，请输入1,2,3,0这4个数字中的一个！")
                    raise ex
                # 手动退出游戏
                if player == 0:

                    # 判断一次没玩就退出游戏
                    if count == 0:
                        print("您还没开始游戏!!!")
                        break

                    print("游戏结束!!!")
                    print("玩家玩了:{}把，赢了:{}把，胜率:{:.2%}" .format(count, player_win, player_win/count))

                    sum_count += count
                    sum_player_win += player_win
                    record_dict = {"count": sum_count, "player_win": sum_player_win}
                    file.write(str(record_dict))
                    break

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
            # 对输入非整数以及其他数据类型进行提示
            except ValueError:
                print("输入非法，请输入整数！")
                print()
            except Exception as res:
                print(res)
                print()
            # 程序运行完成关闭文件
            finally:
                file.close()


play_game()
