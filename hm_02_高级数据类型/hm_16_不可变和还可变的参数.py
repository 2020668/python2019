
def demo(num):

    print("函数内部的代码")

    # 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
    num = 100

    print(num)
    print("函数执行完成")


gl_num = 99
demo(gl_num)
print(gl_num)

# 由于元组修改后，内存地址(引用)不变，所以利用方法修改参数，会修改到外部实参变量


def demo(num_list):

    num_list.append(9)
    print(num_list)


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)

# 列表变量使用 + 不会做相加再赋值，而是调用列表extend方法，整合


def print_into(name, age = 35, gender = True):

    print("name is :%s" % name)
    print("age is :%d" % age)
    print("gender is :%s" %gender)


print_into("夏美", 11)

