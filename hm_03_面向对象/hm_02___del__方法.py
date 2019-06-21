class Cat():

    def __init__(self,new_name):

        self.name = new_name
        print("%s来了" % self.name)

    def __del__(self):

        print("%s去了" % self.name)


tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
# del tom

# 对象销毁之前系统自动调用del方法

print("_"*50)