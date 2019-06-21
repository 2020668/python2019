def sum_2_num(num1,num2):
    """对两个数字的求和"""

    result = num1 + num2

    # 使用返回值，告诉调用函数一方计算的结果
    return result
    # return 下方代码不会被执行
    # num = 1000

# 使用变量接收函数执行的返回结果
sum_result = sum_2_num(10,20)
print("计算结果是:%d" % sum_result)

