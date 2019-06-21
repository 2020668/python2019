class Games(object):

    # 类属性，历史最高分
    top_score = 0

    def __init__(self, play_name):

        self.player_name = play_name

    # 静态方法
    @staticmethod
    def show_help():
        print("帮助信息:让僵尸进入大门...")

    # 类方法
    @classmethod
    def show_top_score(cls):

        print("历史最高分是%d" % cls.top_score)

    # 实例方法
    def play_games(self):

        print("%s开始游戏了..." % self.player_name)


# 查看帮助信息
Games.show_help()

# 查看历史最高分
Games.show_top_score()

# 创建实例对象
xiaoming = Games("小明")
xiaoming.play_games()
