students = [{"name":"小明"},
            {"name":"小美"}]
find_name = "小美"
for stu_dict in students:

    # print(stu_dict)

    if stu_dict["name"] == find_name:

        print("找到%s了" % find_name)
        break

else:
        print("很抱歉，没有找到%s" % find_name)

print("程序结束")
