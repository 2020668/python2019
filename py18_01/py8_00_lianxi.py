# # 3、编写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# def test(num):
#     if len(num) > 5:
#         print(len(num))
#         print("输入数据长度大于5！")
#
#     else:
#         print(len(num))
#         print("输入数据长度不大于5！")
#
#
# test_num = eval(input("请输入字符串，列表或元组,字符串请加上引号："))
#
# test(test_num)


# # 4、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# def test(num):
#     if len(num) > 2:
#         print("[%s, %s]" % (num[0], num[1]))
#     else:
#         print(num)
#
#
# test_list = eval(input("请输入一个列表："))
# test(test_list)


# # 5. 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
# def test(num, nums):
#     if num not in nums.values():
#         nums["new_value"] = num
#
#         print(nums)
#
#
# test_dict = {"name": "小明", "age": "18"}
# test_str = "小明明"
# test(test_str, test_dict)


# # 6. 通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
# def calculation(num1, num2, rules):
#     if rules == "1":
#         print(num1 + num2)
#     elif rules == "2":
#         print(num1 - num2)
#     elif rules == "3":
#         print(num1 * num2)
#     elif rules == "4":
#         print(num1 / num2)
#
#
# num1, num2 = eval(input("请输入两个数字,之间用逗号隔开："))
# rules = input("【1】加 【2】减 【3】乘 【4】除，请输入要进行的运算：")
# calculation(num1, num2, rules)


# # 7、一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。
# #    编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
# member = {}
# count = 0
# met_count = 0
#
#
# def laladui(num):
#     global met_count
#     if num["gender"] == "女" and num["age"] >= 15:
#         print("可以加入球队！")
#         met_count += 1
#
#
# while True:
#     gender, age = eval(input("请输入性别，年龄："))
#     member["gender"] = gender
#     member["age"] = age
#     laladui(member)
#     count += 1
#     if count == 2:
#         print()
#         print("符合条件的人数是：%d" % met_count)
#         break


# # 7、一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。
# #    编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
member = {}
count = 0
met_count = 0


def laladui(num):
    global met_count
    if num["gender"] == "女" and 15 <= num["age"] <= 20:
        print("可以加入球队！")
        met_count += 1
    else:
        return


while True:
    gender, age = eval(input("请输入性别(加引号)，年龄："))
    member["gender"] = gender
    member["age"] = age
    laladui(member)
    count += 1
    if count > 5:
        print()
        print("已经询问过%d个人" % count)
        print("符合条件的人数是：%d" % met_count)
        break

