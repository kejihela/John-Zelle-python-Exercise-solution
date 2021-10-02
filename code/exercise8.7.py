import math
def main():
    print("This program will print the prime number that gives an even number")
    n = int(input("please input your number "))
    v = n + 0
    not_prime = []
    answer = []
    answer2 = []
    prime = []
    if n%2==0:
        if n>2:
            for i in range(n):
                x = round(math.sqrt(n))
                for i in range(2, x+1):
                    if n%i ==0:
                        not_prime.append(n)
                        break
                    else:
                        answer.append(n)
                        for i in answer:
                            if i not in answer2:
                                answer2.append(i)
                n = n-1
        else:
            print("The formular wont work")
    else:
        print("you entered an odd number")
    for i in answer2:
        if i not in not_prime:
            prime.append(i)
    print(prime)
    for i in prime:
        for j in prime:
            total = i + j;
            if total == v:
                print(i,j)
                break
            else:
                continue
               
               
        
main()            
          
