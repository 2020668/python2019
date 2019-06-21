# def print_line(char):
#
#     print(char * 50)
#
#
# print_line("+")


# def print_line(char,times):
#
#     print(char * times)
#
#
# print_line("+",130)


def print_lines(char,times):
    """
    打印多行分割线
    :param char: 分割线的字符串类型
    :param times: 重复的次数
    """
    row = 0
    while row < 5:

        print(char * times)

        row += 1


print_lines("+",50)


