line=int(input(">>>"))
if line%2==0:
    print("请输入一个奇数")
else:
    for i in range(-line//2,line//2+1):
        if i <0:
            print(" "*(-i)+"*"*(line+2*i))
        else:
            print(" "*(i)+"*"*(line-2*i))

