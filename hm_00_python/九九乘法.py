for i in range(1,10):
    s=""
    for j in range(1,i+1):
            s+=str(j)+"*"+str(i)+"="+str(i*j)+" "
    print(s)



#
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d * %d = %d" % (j, i, j*i), end="\t")
#         j += 1
#     print("")
#     i += 1
