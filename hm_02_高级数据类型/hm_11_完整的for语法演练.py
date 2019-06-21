for num in [0, 1, 2, 3]:

    print(num)

# 如果循环体内部使用了break，则else下方代码不会执行
else:
    print("还会执行吗？")

print("演练结束")


for num in [0, 1, 2, 3]:

    print(num)
    if num == 2:
        break
# 如果循环体内部使用了break，则else下方代码不会执行
else:
    print("还会执行吗？")

print("演练结束")
