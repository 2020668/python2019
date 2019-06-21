class Gun:

    def __init__(self, model):

        self.model = model
        self.bullet_count = 1

    def add_count(self, count):

        self.bullet_count += count

    def shoot(self):

        if self.bullet_count <= 0:
            print("%s没有子弹了" % self.model)
            return

        self.bullet_count -= 1
        print("%s突突突...[%d]" % (self.model, self.bullet_count))
