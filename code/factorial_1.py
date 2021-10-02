def factorial():
    print("This program is going to compute the factorial of numbers")
    n = int(input("Please input your number "))
    fact = 1
    for factors in range(n, 1, -1):
        fact = factors * fact
    print("The factorial of ", n , "is ", fact)
factorial()
    
