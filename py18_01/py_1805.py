# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/4/27

E-mail:keen2020@outlook.com

=================================


"""


# # 第一题，输出九九乘法表

# for i in range(1, 10):
#
#     for j in range(1, i+1):
#         print("%d*%d=%d" % (j, i, i*j), end="\t")
#
#     print()
#
#
# # 第二题，利用for循环，完成a=[1,7,4,89,34,2]的从小到大排序（不能使用列表的sort方法）
a = [1, 7, 4, 89, 34, 2, 100, 0, 2, 22, 56]
c = len(a)
b = []
while len(b) < c:
    for i in a:
        if i == min(a):
            b.append(i)
            a.remove(i)
print(b)


# a = [1, 7, 4, 89, 34, 2, 100, 0, 2, 22, 56]
# b = []
# for i in range(min(a), max(a)+1):
#     for j in a:
#         if i == j:
#             b.append(j)
# print(b)


# a = [1, 7, 4, 89, 34, 2, 100, 0]
# for i in range(0, len(a)-1):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)




#
#
# 第三题 有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？abc （a!=b!=c）
# 先将这四个数字组成一个列表
# count = 0
# m = [1, 2, 3, 4]
# for a in m:
#     for b in m:
#         for c in m:
#             if a != b and b != c and a != c:
#                 count += 1
#                 print(a, b, c)
# print()
# print("能组成%d 个不相同且无重复的3位数" % count)
#
#
# # 第四题 对第四次作业的石头剪刀布游戏升级，游戏一轮出拳后进入下一轮，可以手动结束游戏，
# # 手动结束游戏后，打印本次游戏的胜率（胜利的把数除以玩的总把数）
# # 提示：（想办法记录一下计算胜率需要的数据，然后就可以算出结果）

# def play_game():
#
#     # 总把数
#     count = 0
#     # 胜率把数
#     player_win = 0
#
#     while True:
#         import random
#         computer = random.randint(1, 3)
#         player = int(input("请输入数字，1剪刀，2石头，3布,0手动退出："))
#
#         # 手动退出游戏
#         if player == 0:
#
#             # 判断一次没玩就退出游戏
#             if count == 0:
#                 print("您还没开始游戏!!!")
#                 break
#
#             print("游戏结束!!!")
#             print("玩家玩了:%d把，赢了:%d把，胜率:%.2f%%" % (count, player_win, player_win/count * 100))
#             break
#
#         # elif player < 1 or player > 3:
#         elif player not in (1, 2, 3):
#             print("请输入1-3之间的数字")
#             # 增加换行，美化显示效果
#             print()
#             continue
#
#         # 把数计数
#         count += 1
#
#         print("电脑出拳为：%d" % computer)
#         if player == computer - 1 or player == computer + 2:
#             print("玩家胜利！")
#
#             # 玩家胜利计数
#             player_win += 1
#
#         elif player == computer:
#             print("平局！")
#         else:
#             print("电脑胜利")
#
#         print()
#
#
# play_game()


# 第五题，设计图书管理系统
# 数据库的账号信息
Account = {"name": "python18", "password": "lemonban"}
# 存放图书编号，提供为查询提供支持
book_list = []

# # 登录页面
# while True:
#     account = input("请输入账号：")
#     pwd = input("请输入密码:")
#     if account == Account["name"] and pwd == Account["password"]:
#         print("账号密码正确，登录成功！")
#         print()
#         print("================欢迎进入图书管理系统================")
#         print()
#
#         # 主菜单选择模块
#         def show_menu():
#
#             print("【1】：添加图书")
#             print("【2】：修改图书")
#             print("【3】：查询图书")
#             print("【4】：删除图书")
#             print("【5】：显示所有图书")
#             print("【6】：退出系统")
#             print()
#             print("=" * 30)
#             print()
#
#         # 添加图书模块
#         def add_books():
#
#             print("进入图书添加页面！")
#             print()
#
#             # 接收添加图书信息
#             book = {"book_num": "", "book_name": "", "booK_location": ""}
#             book_num = input("请输入图书编号：")
#             book_name = input("请输入图书名称：")
#             book_location = input("请输入存放位置：")
#             book["book_num"] = book_num
#             book["book_name"] = book_name
#             book["book_location"] = book_location
#
#             # 将添加的图书信息存入图书清单
#             book_list.append(book)
#             print("图书编号：%s \n图书名称:%s \n存放位置：%s" % (book["book_num"], book["book_name"], book["book_location"]))
#             print("添加完成，返回主菜单！")
#             print("=" * 30)
#             print()
#
#
#         # 查询图书模块
#         def search_book():
#
#             print("欢迎进入查询图书页面！")
#             print()
#             while True:
#                 book_num = input("请输入要查询的图书编号,退出按N：")
#                 if book_num == "N":
#                     break
#
#                 # 检索图书编号，将输入的数据与数据库比对
#                 for i in book_list:
#                     if book_num == i["book_num"]:
#                         print()
#                         print("="*30)
#                         print("图书编号：%s \n图书名称:%s \n存放位置：%s" % (i["book_num"], i["book_name"], i["book_location"]))
#                         print()
#
#                     else:
#                         print()
#                         print("图书编号不存在，请重新输入：")
#                         print("=" * 30)
#                         print()
#
#         # 修改图书模块
#         def modify_book():
#             print("欢迎进入修改图书页面！")
#             print()
#             while True:
#
#                 book_num = input("请输入图书编号,退出按N:")
#                 if book_num == "N":
#                     break
#
#                 for i in book_list:
#
#                     if book_num == i["book_num"]:
#                         new_num = input("请输入新图书编号：")
#                         new_name = input("请输入新图书名称：")
#                         new_location = input("请输入新存放位置：")
#                         i["book_num"] = new_num
#                         i["book_name"] = new_name
#                         i["book_location"] = new_location
#                         print()
#                         print("成功修改图书！")
#                         print("图书修改后的信息")
#                         print("图书编号：%s \n图书名称:%s \n存放位置：%s" % (i["book_num"], i["book_name"], i["book_location"]))
#                         print()
#
#                     else:
#                         print()
#                         print("图书编号不存在！")
#                         print()
#
#         # 删除图书模块
#         def del_book():
#             print("欢迎进入图书删除页面")
#             print()
#             while True:
#                 del_num = input("请输入要删除图书编号，退出按N：")
#
#                 if del_num == "N":
#                     break
#
#                 for i in book_list:
#                     if del_num == i["book_num"]:
#                         su = input("确认删除！是/Y ,否/N:")
#                         if su == "Y":
#                             book_list.remove(i)
#                             print("图书删除成功！")
#                             print()
#
#                         elif su == "N":
#                             break
#
#                         else:
#                             print("您的输入有误，请重新输入！")
#
#                     else:
#                         print("图书编号不存在，请重新输入：")
#                         print()
#
#         # 显示全部图书模块
#         def show_book():
#             print("全部图书信息如下：")
#             print("="*50)
#             print()
#             for i in book_list:
#                 print("图书编号：%s \n图书名称:%s \n存放位置：%s" % (i["book_num"], i["book_name"], i["book_location"]))
#                 print("="*50)
#
#
#         # 主程序
#         while True:
#             show_menu()
#             request = int(input("请输入您选择的功能："))
#
#             if request == 1:
#                 add_books()
#
#             elif request == 2:
#                 modify_book()
#
#             elif request == 3:
#                 search_book()
#
#             elif request == 4:
#                 del_book()
#
#             elif request == 5:
#                 show_book()
#
#             elif request == 6:
#                 print("已退出图书管理系统！")
#                 print("=" * 30)
#                 break
#
#             else:
#                 print("您的输入有误，请重新输入！")
#
#     # 对错误的账号密码进行提示
#     else:
#         print("您的输入的账号或密码错误，请重新输入！")
#         print()
#         print("=" * 30)
#         print()

