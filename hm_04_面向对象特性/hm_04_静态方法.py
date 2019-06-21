class Dog(object):

    @staticmethod
    def run():
        # 不需要访问实例属性/类属性
        print("小狗要跑了")

Dog.run()
