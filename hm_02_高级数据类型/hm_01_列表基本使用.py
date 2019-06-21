name_list = ["zhangsan","lisi","wangwu"]
# print(name_list[2])

# 索引，取出索引 index
# print(name_list.index("wangwu"))

# 修改
# name_list[0] = "张三"
# print(name_list)

# 增加 append 可在列表末尾追加一个数据
name_list.append("王小二")
print(name_list)

# 增加 insert 可在列表指定索引位置添加数据
name_list.insert(1, "小美眉")
print(name_list)

# 增加 extend 可将另外一个列表的内容添加到当前列表
temp_list = ["大师兄", "朱二哥", "沙师弟"]
name_list.extend(temp_list)
print(name_list)

# 删除 remove 可将指定数据删除
name_list.remove("wangwu")
print(name_list)

# 删除 pop 默认可将列表最后一个数据删除，也可删除指定索引位置的数据
name_list.pop()
print(name_list)

name_list.pop(3)
print(name_list)

# 删除 del 将一个变量从内存中删除

del name_list[1]
print(name_list)
