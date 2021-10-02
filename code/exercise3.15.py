import math
pi = math.pi
def pi_approx():
    print("This program will print the approximate error value of pi")
    n = int(input("how many numbers did you want to sum? "))
    accumulator = 0
    for i in range(n):
        x = eval(input("please input your numbers "))
        accumulator = accumulator + x
    error = pi - accumulator
    print("the difference between pi and the value is", error)
    
pi_approx()
        
    
