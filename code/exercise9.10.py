from random import random
def main():
    Introduction()
    a = getInputs()
    h, n = simulation(a)
    Results(h, n)
   

def Introduction():
    print("program that accepts the number of darts as an input and")
    print("then performs a simulation to estimate the value of pi")
def getInputs():
    while True:
        a = int(input("How many darts did you want to throw "))
        if a <= 0:
            print("Please enter value above 0")
        else:
            return a
def simulation(a):
    h_list = []
    n_list = []
    h = n = 0
    for i in range(a):
        b = random()
        c = random()
        x = (2 * b) - 1
        y = (2 * c) - 1
        x_sqr = x * x
        y_sqr = y * y
        x_y = x_sqr + y_sqr
        if x_y <=1:
            h = h + 1
            n = n + 1 
        else:
            n = n + 1 

    return h, n

def Results(h, n):
    total = h + n
    print(h,n)
   
    print("\n total number of simulation is", total)
    pi = 4*(h/n)
    print("\n Approximate value of pi is", pi)
        


if __name__ == '__main__' : main()
    
    
