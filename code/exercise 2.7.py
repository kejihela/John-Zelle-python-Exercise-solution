def investment():
   
    apr = eval(input("pls, input your investment rate "))
    n = eval(input("ow many yers do you want to invest" ))
    investment = []
    total = 0
    for i in range(n):
        principal = eval(input("pls, insert your capital "))
        interest = int(principal * (1 + apr))
        investment.append(principal)
        print("your interest is ", interest)
    print(investment)
    for i in investment:
        total = i + total
    print(total)
investment()
