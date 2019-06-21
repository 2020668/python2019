# class Animal ():
#
#     def eat(self):
#         print("吃")
#
#     def drink(self):
#         print("喝")
#
#     def run(self):
#         print("跑")
#
#     def sleep(self):
#         print("跑")
#
#
# # 继承的方法
# class Dog(Animal):
#
#     def bark(self):
#         print("汪汪叫")
#
#
# xiaohuang = Dog()
# xiaohuang.run()
#
#
# class XiaoTianquan(Dog):
#
#     # 在子类中重写父类方法
#     def bark(self):
#         print("像神一样叫唤")
#
#     # 使用super().调用原本在父类中封装的方法
#
#         super().bark()
#         print("%##$%&**")
#
#
# xtq = XiaoTianquan()
# xtq.bark()

#
# class Dog:
#
#     def __new__(cls, *args, **kwargs):
#
#     def __init__(self, name):
#         self.name = name
#
#     def bark(self):
#         print("汪汪叫")
#
#
# class Xiaotianquan(Dog):
#
#     def bark(self):
#         print("%s像神一样叫唤" % self.name)
#
#
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def game_with_dog(self, dog):
#         print("%s和%s 快乐的玩耍" % (self.name, dog.name))
#         dog.bark()
#
#
# # wangcai = Dog("旺财")
# wangcai = Xiaotianquan("哮天犬")
# xiaoming = Person("小明")
# xiaoming.game_with_dog(wangcai)


class Music(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if self.init_flag:
            return
        print("初始化播放器")
        self.init_flag = True


player1 = Music()
player2 = Music()
print(player1)
print(player2)




