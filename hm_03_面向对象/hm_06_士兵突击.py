# 枪类
class Gun(object):

    def __init__(self, model):

        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        if self.bullet_count <= 0:
            print("%s没有子弹了..." % self.model)
            return

        self.bullet_count -= 1

        print("[%s]突突突...[%d]" % (self.model,self.bullet_count))


# 士兵类
class Soldier(object):

    def __init__(self, name):

        self.name = name
        self.gun = None

    def fire(self):

        if self.gun is None:
            print("%s还没有枪" % self.name)

            return
        print("冲啊...[%s]" % self.name)

        self.gun.add_bullet(50)

        self.gun.shoot()


# 主程序
ak47 = Gun("AK47")
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()


