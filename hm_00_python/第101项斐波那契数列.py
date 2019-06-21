a=0
b=1
c=0
count=0
while True:
    c=a+b
    if count==99:
        print(c,end=",")
        break
    a=b
    b=c
    count+=1
