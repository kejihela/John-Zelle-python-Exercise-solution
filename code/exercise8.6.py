import math
def main():
    print("This program is about to determine a prime number or not")
    n = int(input("please input your number "))
    not_prime = []
    is_prime = []
    prime = []
    prime1 = []
    
    if n>2:
        for i in range(n):
            x = round(math.sqrt(n))
            for i in range(2, x+1):
                if n%i ==0:
                    ##print(n,"is not a prime number")
                    not_prime.append(n)
                    break
                else:
                    is_prime.append(n)
                    for i in is_prime:
                        if i not in prime:
                            prime.append(i)
                    print(n,"is a prime number")
            n = n-1  
    else:
        print("The formular won't work")
   
    for i in prime:
        if i not in not_prime:
            prime1.append(i)
    print(prime1)
                
main()
            
