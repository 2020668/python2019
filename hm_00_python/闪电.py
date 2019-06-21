n=int(input("请输入一个奇数>>>"))
e=n//2
for i in range(-e,n-e):
    if i<0:
        print(" "*(-i)+"*"*(e+1+i))
    elif i>0:
        print(" "*(e)+"*"*(e+1-i))
    else:
        print("*"*(n))
        

