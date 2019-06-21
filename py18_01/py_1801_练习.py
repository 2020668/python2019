# Account = {}
# def register():
#     print("="*50)
#     print("欢迎进入注册页面")
#     register_name = input("请输入用户名：")
#
#     register_pwd = input("请输入密码：")
#     if len(register_name) == 0 or len(register_pwd) == 0:
#         print("输入的账号或密码为空！")
#     else:
#         Account["name"] = register_name
#         Account["pwd"] = register_pwd
#         print("注册成功!")
#         print(Account)
#
#
# register()


def input_password():
    pwd = input("请输入密码：")
    if len(pwd) > 8:
        return pwd
    # 创建异常对象，对异常进行说明
    ex = Exception("密码长度不够")
    # 抛出异常，供程序捕获
    raise ex


print(input_password())
