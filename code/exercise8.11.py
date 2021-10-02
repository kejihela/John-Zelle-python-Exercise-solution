def main():
    print("This program is about to print the coolness and hotness")
    days = int(input("How many days of temperature do you want to compute "))
    hdd=0
    cdd=0
    temp = int(input("what is today average temperature "))
    for i in range(days-1):
        if temp < 60:
            hdd = hdd + (60 - temp)
        elif temp > 80:
            cdd = cdd + (temp - 80)
        temp = int(input("what is today average temperature "))
        
    print("hot degree days",hdd, "cold degree days",cdd)
main()
        
            
               
        
        
        
               
