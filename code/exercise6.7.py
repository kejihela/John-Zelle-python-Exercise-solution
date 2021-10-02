def fibonacci(n, x, y):
    for i in range(n-1):
        acc = x + y
        x = y
        y =acc
    return acc
        
def main():
    print("this will compute fibonacci number")
    n = int(input("please input your value "))
    fibo = fibonacci(n, 0 ,1)
    print(fibo)
main()
    
    
            
            
