def fibonacci():
    print("This program will print the fibonacci of numbers")
    n = int(input("how many numbers do you want to calculate for? "))
    x = 0
    y = 1
    for i in range(n-1):
        ans = x + y
        x = y
        y = ans
    print("The fibonacci number for the series is", y)
fibonacci()
        
        
