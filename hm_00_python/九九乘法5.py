for i in range(1,10):
    s=""
    for j in range(i,10):
        s += str(i) + "*" + str(j) + "=" + str(i * j) + " "
    if (i*j)<10:
        print("{:>54}".format(s))
    else:
        print("{:>57}".format(s))
    
