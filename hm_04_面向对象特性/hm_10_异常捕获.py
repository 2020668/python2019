# def demo1():
#     num = int(input("请输入一个整数:"))
#     num1 = 8 / num
#     print(num1)
#
#
# def demo2():
#     return demo1()
#
# # 利用函数的传递性，在主程序捕获异常
#
#
# try:
#     print(demo2())
#
# except Exception as result:
#     print("未知错误%s" % result)


def input_password():

    pwd = input("请输入密码")

    if len(pwd) >= 8:
        return pwd

    # 创建异常对象，可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 抛出异常
    raise ex


try:
    print(input_password())

except Exception as result:
    print(result)
