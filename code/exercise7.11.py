def main():
    print("This program is to run a leap year")
    year = int(input("Please input your year "))
    if year%4 == 0:
        if year%100==0 and year%400==0:
            print("this is a leap year")
        elif year%100==0:
            print("This is not leap year nah")
        else:
            print("this is a leap year for 4") 
    else:
        print("This is not a leap year")
        
main()
    
               
