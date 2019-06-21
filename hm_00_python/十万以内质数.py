import datetime
start=datetime.datetime.now()
number=100000
count=2
sum=0
for num in range(4,number):
    if num%6!=1 and num%6!=5:
        continue
    else:
        snum=int(num**0.5+1)
        for i in range(5,snum):
            sum+=1
            if not num%i:
                break
        else:
            count+= 1
print(count)
print(sum)
delta=(datetime.datetime.now()-start).total_seconds()
print(delta)
