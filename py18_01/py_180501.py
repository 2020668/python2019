# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/5/2

E-mail:keen2020@outlook.com

=================================


"""


# 存储账号信息，用于登录信息比对。已存在一个账号，用于初始比对新注册账号用户名是否已存在
member = [{"name": "root", "pwd": "python"}]
account = {}
# 存储图书清单，用于查询等操作
book_list = []
# 存储图书编号，用于后续操作首先识别输入的图书编号是否正确
book_id_list = []
# 存储图书名称，用于后续操作首先识别输入的图书名称是否正确
book_name_list = []


# 欢迎页面
def login_menu():
    while True:
        print("="*50)
        print("欢迎访问图书管理系统！")
        print("【1】注册  【2】登录")
        login_request = input("请输入功能选项：")
        if login_request in ["1", "2"]:
            if login_request == "1":
                register()
            if login_request == "2":
                login()
                break
        else:
            print("输入有误，请重新输入！")


# 注册成功后，将账号密码存入users文件中
def register():
    with open("users", "a+") as file:
        print("="*50)
        print("欢迎进入注册页面")
        register_name = input("请输入用户名：")
        for test_name in member:
            if register_name in test_name["name"]:
                print("账号已存在！")
                break
            register_pwd = input("请输入密码：")
            if len(register_name) == 0 or len(register_pwd) == 0:
                print("输入的账号或密码为空！")
            else:
                account["name"] = register_name
                account["pwd"] = register_pwd
                # 将账号密码存入users文件
                file.write(str(account)+"\n")
                print("注册成功!")


# 登录
def login():
    while True:
        print("="*50)
        print("欢迎来到登录页面！")
        login_name = input("请输入用户名：")
        login_pwd = input("请输入密码：")
        if login_name == account["name"]and login_pwd == account["pwd"]:
            print("登录成功！")
            return

        else:
            print("账号或密码错误，请重新输入！")


# 主菜单
def show_menu():
    while True:
        print("="*50)
        print("欢迎登录图书管理系统！")
        print("【1】增加图书 【2】显示所有图书 【3】修改图书 【4】查找图书 【5】删除图书 【6】退出系统")
        show_request = input("请选择功能：")
        if show_request == "1":
            add_book()
        elif show_request == "2":
            all_book()
        elif show_request == "3":
            update_book()
        elif show_request == "4":
            find_book()
        elif show_request == "5":
            del_book()
        elif show_request == "6":
            print("已退出图书管理系统！")
            break
        else:
            print("输入有误，请重新输入！")


# 添加图书
def add_book():
    print("="*50)
    print("欢迎进入添加图书页面！")
    book = {}
    add_id = input("请输入图书编号：")
    # 对重复图书编号进行提示
    if add_id not in book_id_list:
        add_name = input("请输入图书名称：")
        add_location = input("请输入图书存放位置：")
        book["id"] = add_id
        book_id_list.append(add_id)
        book["name"] = add_name
        book_name_list.append(add_name)
        book["location"] = add_location
        book_list.append(book)
        print("新增图书成功！")
        print()
    else:
        print("编号%s已存在！" % add_id)


# 显示图书
def all_book():
    print("="*50)
    print("显示所有图书")
    print()
    for show_book in book_list:
        print("图书编号：%s\n图书名称：%s\n存放位置：%s" % (show_book["id"], show_book["name"], show_book["location"]))
        print()


# 修改图书
def update_book():
    print("="*50)
    print("欢迎进入修改图书页面！")
    update_id = input("请输入图书编号：")
    # 对输入的图书编号进行判断
    if update_id in book_id_list:
        for up_book in book_list:
            if up_book["id"] == update_id:
                up_location = input("请输入新位置：")
                up_book["location"] = up_location
                print("修改成功！")

    # 对输入的图书编号错误进行提示
    else:
        print("图书编号不存在！")


# 查找图书，先根据图书名称查询，然后从同名图书中选择一本(输入编号)
def find_book():
    print("="*50)
    print("欢迎进入查询图书页面！")
    # 存储按图书名称查询的结果
    fd_book_list = []
    while True:
        fd_name = input("请输入图书名称，返回上一步按N：")
        # 退出操作选项
        if fd_name == "N":
            break
        # 输入图书名称正确，才进行查询
        if fd_name in book_name_list:
            print("查询结果")
            for fd_book in book_list:
                if fd_book["name"] == fd_name:
                    fd_book_list.append(fd_book)
                    book_id_list.append(fd_book["id"])
                    print("图书编号%s\n图书名称：%s\n存放位置：%s" % (fd_book["id"], fd_book["name"], fd_book["location"]))
                    print()
        # 对输入图书名称不正确的提示，并返回输入图书名称界面
        else:
            print("图书【%s】不存在" % fd_name)
            continue

        # 从按图书名称查询结果中选择一本图书，输入图书编号
        while True:
            fd_new_id = input("请选择一本图书的编号，返回上一步按N：")
            if fd_new_id == "N":
                break
            # 输入正确的图书编号，才继续查询
            if fd_new_id in book_id_list:
                print("查询结果")
                for fd_new_book in fd_book_list:
                    if fd_new_id == fd_new_book["id"]:
                        print("图书编号：%s\n图书名称：%s\n存放位置：%s" %
                              (fd_new_book["id"], fd_new_book["name"], fd_new_book["location"]))
                        print()
            # 对输入错误图书编号的提示
            else:
                print("图书编号【%s】不存在" % fd_new_id)
                # 返回输入图书名称界面
                break


# 删除图书
def del_book():
    print("=" * 50)
    print("欢迎进入删除图书页面！")
    del_id = input("请输入图书编号：")
    if del_id in book_id_list:
        for de_book in book_list:
            if de_book["id"] == del_id:
                book_list.remove(de_book)
                print("删除成功！")

    # 对输入的图书编号错误进行提示
    else:
        print("图书编号不存在！")


# 主程序
def main():
    login_menu()
    show_menu()


if __name__ == '__main__':
    main()
