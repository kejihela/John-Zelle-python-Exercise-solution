def fibonacci(n):
    x = 1 
    y = 1
    for i in range(n-1):
        acc = x + y
        y = x
        x = acc
    print("The fibonacci of", n , "is", x)
        
def main():
    print("This program will print the fibonacci of numbers")
    a = int(input("the nth number for the fibonacci "))
    fibonacci(a)
main()
    
