class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "我叫%s,我的体重是%.2f公斤" % (self.name, self.weight)

    def run(self):

        print("%s爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):

        print("%s爱吃东西" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75)

xiaoming.eat()
xiaoming.run()
print(xiaoming)

xiaomei = Person("小美", 50)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
