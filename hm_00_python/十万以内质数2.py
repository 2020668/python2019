import datetime
start=datetime.datetime.now()
number=100000
count=1
sum=0
for i in range(3,100000,2):
    for j in range(3,int(i**0.5+1),2):
        sum+=1
        if not i % j:
            break
    else:
        count+=1
print(count)
print(sum)
delta=(datetime.datetime.now()-start).total_seconds()
print(delta)