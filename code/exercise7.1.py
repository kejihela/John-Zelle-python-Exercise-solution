def wages(time, rate):
    if time <=40:
        wage = rate * time
        return wage
    else:
        hour = time - 40
        wage = hour * (rate/2) + 40 * rate
        return wage
def main():
    print("This program will print wages of workers")
    t = int(input("input the numbers of hour work "))
    r = int(input("how much per hour "))

    result = wages(t,r)
    print(result)
main()
            
    
    
