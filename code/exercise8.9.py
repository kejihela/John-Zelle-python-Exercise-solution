def main():
    print("This program will compute the fuel efficiency of multi leg journey")
    odometer = eval(input("Please what is the starting odometer reading "))
    leg1 = str(input("please what is the current odometer and gas used "))
    leg2 = str(input("please what is the current odometer and gas used "))
    leg3 = str(input("please what is the current odometer and gas used "))
    leg4 = str(input("please what is the current odometer and gas used "))
    print("End of the trip")

    odo1,gas1 = leg1.split()
    odo2,gas2 = leg2.split()
    odo3,gas3 = leg3.split()
    odo4,gas4 = leg4.split()

    mpg1 = (int(odo1) - odometer)/int(gas1)
    mpg2 = (int(odo1) - odometer)/int(gas2)
    mpg3 = (int(odo1) - odometer)/int(gas3)
    mpg4 = (int(odo1) - odometer)/int(gas4)

    total_mpg =mpg1+mpg2+mpg3+mpg4
    print(mpg1,"",mpg2,"",mpg3,"",mpg4)
    print(total_mpg)
main()
    
                          
    
                    
