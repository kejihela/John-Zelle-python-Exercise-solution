def interest_rate_mod():
    print("The interest rate calculation based on users input ")
    n = eval(input("please enter the number of years for your investment "))
    apr = eval(input("please, input the interest rate "))
    principal = eval(input("please input the value of your capital "))
    for i in range(n):
        i = i + 1
        principal = principal * (1 + apr)
        print("the vaalue of principal after", i , "year is", principal)

interest_rate_mod()
