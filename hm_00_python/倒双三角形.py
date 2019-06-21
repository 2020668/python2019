n=int(input("请输入一个奇数>>>"))
e=n//2
for i in range(-e,n-e):
    prespace=-i if i<0 else i
    print(" "*(e-prespace)+"*"*(2*prespace+1))


