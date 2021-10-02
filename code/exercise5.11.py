def chaos():
    print("print a chaotic expression")
    x = eval(input("please enter your initial value "))
    y = eval(input("please enter your initial value "))
    n = eval(input("print the number of iterations "))
    for i in range(n):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print("the outputs are ,", x,".......",y)
chaos()
