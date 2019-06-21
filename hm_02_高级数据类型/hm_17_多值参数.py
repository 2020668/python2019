# 参数名前添加一个 * ，可以接收元组。两个 * 可以接收字典。args arguments参数
def demon(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


demon(1)
demon(1, 2, 3, 4, 5,name="小明",age=18)


# 元组和字典的拆包

def demon(*args, **kwargs):

    print("开始拆包...")
    print(args)
    print(kwargs)


# 元组变量，字典变量
gl_num = (1, 2, 3)
gl_dict = {"name":"小明","age": 18}

# demon(gl_num, gl_dict)
demon(*gl_num, **gl_dict)


