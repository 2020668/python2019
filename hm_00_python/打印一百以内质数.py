import math
n=100
lst=[2]
for n in range(3,n):
    for i in lst:
        if n % i ==0:
            break
    else:
        print(n)
        lst.append(n)
