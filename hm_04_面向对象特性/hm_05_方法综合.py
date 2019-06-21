class Game(object):

    # 类属性直接赋值
    top_score = 0
    # 实例属性初始化方法定义
    def __init__(self,player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息")

    # 类方法 方法内部只需访问类属性
    @classmethod
    def show_top_score(cls):
        print("历史最高分%d" % cls.top_score)

    # 实例方法 方法内部需要访问实例属性
    def start_game(self):
        print("%s开始游戏" % self.player_name)


# 查看游戏帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
game = Game("小明")
game.start_game()
