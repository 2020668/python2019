n=6
oldline=[]
newline=[1]
length=0
print(newline)
for i in range(1,n):
    oldline=newline.copy()
    oldline.append(0)#尾部加0
    newline.clear()
    for j in range(i+1):
        newline.append(oldline[j-1]+oldline[j])
    print(newline)
