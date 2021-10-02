def accrue_rate():
    print("This program will print interest for certain years")
    rate = eval(input("enter the rate per year "))
    period = eval(input("pls, input how many times interest should be calculated in a year "))
    principal = eval(input("please enter your principal "))
    for i in range(10 * period):
        principal = principal * (rate/period)
    print(principal)
accrue_rate()
        
