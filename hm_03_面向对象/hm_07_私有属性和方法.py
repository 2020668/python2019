class Women():

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        # 在对象的方法内部，可以访问对象的私有属性
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 私有属性和私有方法，在外界不能够直接访问
xiaofang.secret()
# print(xiaofang.self.__age)

# 伪私有属性和方法
print(xiaofang._Women__age)
