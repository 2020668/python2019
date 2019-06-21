# 于列表类似，不可修改
info_tuple = ("zhangsan",18,1.65)
print(info_tuple.index(18))
print(info_tuple.count("zhangsan"))
print(len(info_tuple))
for i in (info_tuple):
    print(i)

# 元组于列表之间的转换
simple_list = [2,5.5,66,125]
print(list(info_tuple))
print(tuple(simple_list))

