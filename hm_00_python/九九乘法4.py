
for i in range(1,10):
    for j in range(1, i + 1):
        s = i * j
        if j>1 and s<10:
            s = str(s) + " "
        else:
            s = str(s)
        print(str(j) + "*" + str(i) + "=" + s, end=" ")
    print()

for i in range(1,10):
    for j in range(1, i + 1):
        print("%d*%d=%d" %(j,i,i*j),end = "\t")
    print()

i = 1
while i <= 9:
    n = 1
    while n <= i:
        print("%d*%d=%d" %(n,i,i*n),end = "\t")
        n += 1
    print()
    i += 1


