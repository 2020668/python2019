# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/13

E-mail:keen2020@outlook.com

=================================


"""

# 改进图书管理系统
# 注册的时候，将输入的用户名与users文件做比对，存在就提示该用户名已存在
# 注册完成后，将账号密码存入users中，添加图书时，图书编号与books比对，存在提示图书编号已存在
# 添加图书后，将图书信息存入books文件中
# mem_dict = {}
#
# with open("users", "a+", encoding="utf8") as file:
#     user_name = input("请输入用户名：")
#     # 将指针设置首部，才可读取数据
#     file.seek(0)
#     # 读取数据后，指针到达尾部。读取多行数据得到一个list，遍历该list得到str
#     for text in file.readlines():
#         # 将str转换成字典，然后当做数据库来与输入的用户名比对，重复就提示用户名已存在
#         if user_name in eval(text)["name"]:
#             print("用户已存在！")
#             break
#     else:
#         user_pwd = input("请输入密码：")
#         mem_dict["name"] = user_name
#         mem_dict["pwd"] = user_pwd
#         # 此时在数据尾部写入内容
#         file.write(str(mem_dict)+"\n")
#         print("注册成功!")

# book = {}
# with open("books", "a+", encoding="utf8") as file:
#     add_id = input("请输入图书编号：")
#     # file.seek(0)
#     # for text in file.readlines():
#     #     if add_id in eval(text)["id"]:
#     #         print("编号%s已存在！" % add_id)
#     # else:
#     add_name = input("请输入图书名称：")
#     add_location = input("请输入图书存放位置：")
#     book["id"] = add_id
#     book["name"] = add_name
#     book["location"] = add_location
#     file.write(str(book) + "\n")
#     print("新增图书成功！")
#     print()

case_dict = dict(name="xiaoming", data="sanyuan")
print(case_dict)
print(type(case_dict))
