# 递归，特点：一个函数内部调用自己
def sum_number(num):

    print(num)

    # 设置递归出口
    if num == 1:
        return
    # 自己调用自己
    sum_number(num - 1)


sum_number(3)


# 练习题
# 计算1 + 2 + 3 + 4 + 5 + .....num 的结果
def sum_num(num):

    # 递归出口
    if num == 1:
        return 1

    # 接收比num小1的值
    temp = sum_num(num - 1)

    # 从num开始依次叠加递减1的值，并返回结果值，到1的时候返回1，然后退出递归
    return temp + num


result = sum_num(100)
print("叠加结果是：%d" % result)
