import math
def main():
    print("This program is about to determine a prime number or not")
    n = int(input("please input your number "))
    if n>2:
        x = round(math.sqrt(n))
        for i in range(2, x):
            k = n/i
            if k%2 ==0:
                print(n,"is not a prime number")
                break
            else:
                print(n,"is a prime number")
                
    else:
        print("The formular won't work")
                
main()
                
            
