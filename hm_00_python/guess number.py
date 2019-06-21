while True:
    txt=input("请输入一个数字:\n")
    if txt=="stop":
        break
    elif not txt.isdigit():
        print("您输入的不是数字")
    else:
        num=int(txt)
        if num<20:
            print("您输入的数字太小了")
        elif num>20:
            print("您输入的数字太大了")
        else:
            print("恭喜您！猜对了！！")
