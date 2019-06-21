class MusicPlayer(object):

    # 定义类属性为空
    instance = None
    # 定义初始化标记，默认为False
    init_falg = False

    def __new__(cls, *args, **kwargs):

        # 判断类属性是否为空
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 判断是否执行过初始化动作
        if MusicPlayer.init_falg:
            return

        print("初始化播放器")

        MusicPlayer.init_falg = True


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

