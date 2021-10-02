def futval():
    print("this program will print out your investment in total")
    capital = eval(input("please input your capital "))
    rate = eval(input("please input the rate of investment "))
    n = eval(input("please input the number of years for investment"))

    for i in range(n):
        i = i+1
        capital  = capital * (1+rate)
        print("in", i ,"year you receive ", capital)
futval()
             
