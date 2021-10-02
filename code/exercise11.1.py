from math import sqrt

def getNumber():
    num = []
    print("Press spacebar to stop ")
    val = input("please, enter your number ")
    while val != "":
        x = float(val)
        num.append(x)
        val = input("please, enter your number ")
    return num
            
    
def mean(num):
    n = 0
    total = 0
    for x in num:
        n = n + 1
        total = total + x
    mean = total/n
    return mean

def std_dev(num,mean):
    n = 0
    total = 0
    for x in num:
        n = n+1
        total = total + (x-mean)**2
    std_dev = sqrt(total/(n-1))
    return std_dev

def meanStd_dev(num):
    return mean(num), std_dev(num)

def main():
    print("This program will print mean and standard deviation")
    values = getNumber()
    mean_value = mean(values)
    print(mean_value)
    standard_dev = std_dev(values,mean_value)
    print(standard_dev)
    
    


main()
    


        
        
        
            
