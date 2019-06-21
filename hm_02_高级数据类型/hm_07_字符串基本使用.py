char_str = "hello hello"
# 字符串长度
print(len(char_str))
# 字符出现的次数
print(char_str.count("llo"))
# 字符串索引
print(char_str[4])
# 判断空白字符
space_str = " \t\n\r "
print(space_str.isspace())
# 判断字符串中是否包含数字，全角数字
# 全角数字，(1)，\u00b2
# 全角数字，汉字数字
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

# 指定字符串开始startswith 结束endswith
print(num_str.startswith("一"))
print(num_str.endswith("零"))
# 查找，index会报错，find返回-1
print(num_str.find("零"))
# 替换 replace 不会修改原字符串，产生一个新字符串
print(num_str.replace("一","二"))
# rfind rindex从右开始




