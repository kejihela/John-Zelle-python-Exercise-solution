import math
def guess(guess, n, x):
    for i in range(n):
        guess = (guess+(x/guess))/2
    return guess
def root(x):
    sq_rt = math.sqrt(x)
    return  sq_rt
def error(square_root,guess_answer ):
    error = square_root - guess_answer
    return error
    
    
def main():
    print("guess method for computing square root ")
    x = int(input("please input the value to find its root "))
    n = int(input("how many times do you want to improve your guess"))
    initial_guess = x/2
    guess_answer = guess(initial_guess, n, x)
    square_root = root(x)
    print(guess_answer)
    print(square_root)
    error_value = error(square_root,guess_answer)
    print(error_value)
main()
