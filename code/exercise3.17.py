import math
def square_root():
    print("This program will print the square root of a number")
    x = int(input("Please, input your number "))
    n = int(input("how many times do you want to improve your guesses "))
    guess = x/2
    for i in range(n):
        guess = (guess + (x/guess))/2
    print("the square root of ", x , " is approx. ",guess)
    error = math.sqrt(x) - guess
    print("The error value between the guess square root and the original is", error)
square_root()
