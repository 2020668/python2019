class Tool(object):

    # 使用赋值语句定义类属性
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量%d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("扳手")

Tool.show_tool_count()