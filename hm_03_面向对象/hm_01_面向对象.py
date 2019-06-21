# class CatCat:
#
#     def eat(self):
#         print("小猫爱吃鱼")
#
#     def drink(self):
#         print("小猫爱喝水")
#
#
# tom = CatCat()
# tom.eat()
# tom.drink()
# print(tom)

# 初始化方法内部定义属性

# class Cat:
#
#     def __init__(self):
#         print("这是一个初始化方法")
#
#         self.name = "大懒猫"
#
#     def drink(self):
#         print("%s爱喝水" % self.name)
#
#
# tom = Cat()
# tom.drink()


# 改进
class Cat:

    def __init__(self, new_name):
        print("这是一个初始化方法")

        self.name = new_name

    def drink(self):
        print("%s爱喝水" % self.name)


tom = Cat("Tom")
tom.drink()

lazy_cat = Cat("大懒猫")
lazy_cat.drink()


