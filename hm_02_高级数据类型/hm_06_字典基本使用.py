xiaoming_dict = {"name":"小明"}
# 取值
print(xiaoming_dict["name"])
# 增加
xiaoming_dict["age"] = 18
print(xiaoming_dict)
# 修改
xiaoming_dict["age"] = 21
print(xiaoming_dict)
# 统计键值对的数量
print(len(xiaoming_dict))
# 合并字典
temp_dict = {"weight":75.5}
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
# 清空字典
# xiaoming_dict.clear()
# print(xiaoming_dict)
# 迭代遍历字典
for k in xiaoming_dict:
    print("%s - %s" % (k,xiaoming_dict[k]))

# 应用场景，列表中保持字典
card_list = [{"name":"小明",
              "age":15,
              "phone":"10086"},
             {"name":"小华",
              "age":18,
              "phone":"10010"}]
for card_info in card_list:
    print(card_info)

card_dict = {"name":"小明",
              "age":15,
              "phone":"10086"}
print(card_dict)