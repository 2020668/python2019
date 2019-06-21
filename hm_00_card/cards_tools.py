
card_list = []


def show_menu():

    print("*"*50)
    print("欢迎使用【名片管理系统】v 0.0.1")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*"*50)


def new_card():

    print("-"*50)
    print("新增名片")
    name_str = input("请输入姓名: ")
    phone_str = input("请输入电话号码: ")
    qq_str = input("请输入qq号码: ")
    email_str = input("请输入邮箱地址:")
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    card_list.append(card_dict)

    print(card_list)

    print("添加%s 的名片成功" % name_str)


def show_all():

    print("-" * 50)
    print("显示所有名片")

    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t\t")
    print("")
    print("="*50)

    if len(card_list) == 0:
        print("当前没有名片记录，请使用新增名片功能")

        return

    for card_dict in card_list:

        print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (card_dict["name"],
                                                    card_dict["phone"],
                                                    card_dict["qq"],
                                                    card_dict["email"]))


def search_card():

    print("-" * 50)
    print("搜索名片")

    find_name = input("请输入要查找的姓名：")

    for card_dict in card_list:

        if card_dict["name"] == find_name:
            for name in ["姓名", "电话", "qq", "邮箱"]:
                print(name, end="\t\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (card_dict["name"],
                                                        card_dict["phone"],
                                                        card_dict["qq"],
                                                        card_dict["email"]))

            deal_card(card_dict)

            break

    else:
        print("抱歉，没有找到%s" % find_name)


def deal_card(find_dict):

    print(find_dict)

    action_str = input("请输入需要执行的操作 "
                       "1 修改 2 删除 0 返回上级菜单")

    if action_str == "1":

        before_name = find_dict["name"]
        find_dict["name"] = input_card_info(find_dict["name"],"请输入修改后的name[回车不修改]: ")
        find_dict["phone"] = input_card_info(find_dict["phone"],"请输入修改后的phone[回车不修改]: ")
        find_dict["qq"] = input_card_info(find_dict["qq"],"请输入修改后的qq[回车不修改]: ")
        find_dict["email"] = input_card_info(find_dict["email"],"请输入修改后的email[回车不修改]: ")

        print("%s 的名片修改成功" % before_name)

    elif action_str == "2":

        sure_str = input("确定要删除%s的名片吗 Y or N:" % find_dict["name"])

        if sure_str == "Y":

            card_list.remove(find_dict)
            print("删除%s的名片成功" % find_dict["name"])

        elif sure_str == "N":

            return

        else:
            print("您的操作有误，请重新输入")


    else:

        print("返回上级菜单")


def input_card_info(dict_value,tip_message):

    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str

    else:
        return dict_value
