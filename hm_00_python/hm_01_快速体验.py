import hm_00_封装函数
hm_00_封装函数.multiple_table()


def say_hell0():
    """打招呼"""

    print("hello")
    print("hello")
    print("hello")


say_hell0()


def sum_2_num(num1,num2):
    """两个数字的求和"""

    result = num1 + num2
    print("%d + %d = %d" % (num1,num2,result))


sum_2_num(20,120)


def sum_2_num(num1,num2):
    """两个数字的求和"""


    result = num1 + num2
    return result


sum_result = sum_2_num(20,120)

print("计算结果：%d" % sum_result)




