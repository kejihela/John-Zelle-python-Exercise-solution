def investment():
    print("this calculate the value of principal in the next ten years")
    apr = eval(input("pls, input the value of your interest rate "))
    principal = eval(input("pls, input the value of your principal "))
    answer = principal * (1+apr)
    
    for i in range(1, 101):
        principal = principal * (1+apr)
        print("the interest for the", i , "year", principal)
        
investment()
