def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 30
    wetness = 50
    print("测量结束")

    # 元组可以包含多个数据，可使用元组让函数一次返回多个值
    # 如果函数返回的结果是元组，小括号可以省略
    return temp, wetness

# result = measure()
# print("温度是:%d" % result[0])
# print("湿度是:%d" % result[1])
# 如果函数的返回类型是元组，同时希望单独的处理元组中的元素，可使用多个变量接收返回结果，个数保持一致


gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)
