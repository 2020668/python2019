# 全局变量
num = 10

def demon1():

    # 希望修改全局变量的值，使用global声明一下变量即可
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时就不会创建局部变量   全局变量命名gl_
    # global num

    num = 99

    print("demon1 ==> %d" % num)


def demon2():
    print("demon2 ==> %d" % num)


demon1()
demon2()

