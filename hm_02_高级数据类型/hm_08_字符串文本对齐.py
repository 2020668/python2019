poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:

# print("|%s|" % poem_str.center(10, "　"))
# 左右对齐，ljust rjust

    print("|%s|" % poem_str.ljust(10, "　"))
# 去除空白字符,左边string.lstrip()，两边strip()，右边string.rstrip()

poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:

    # 去除空白字符

    poem_str.strip()
    print("|%s|" % poem_str.strip().center(10, "　"))
