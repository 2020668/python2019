poem_str = "\t\n登鹳雀楼\t王之涣白日依山尽\t\n黄河入海流\n欲穷千里目\t更上一层楼"
print(poem_str)
# 1.将空白字符全部去除
# 2.再使用" "作为分隔符，
poem_list = poem_str.split()
print(poem_list)
result = " ".join(poem_list)
print(result)