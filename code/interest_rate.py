def interest_rate():
    print("this calculate the value of principal in the next ten years")
    apr = eval(input("pls, input the value of your interest rate "))
    principal = eval(input("pls, input the value of your principal "))
    for i in range(10):
        principal = principal * (1 + apr)
        print("the principal in the next 10 years are: ", principal)
    input("press enter key to quit")
interest_rate()
                     
