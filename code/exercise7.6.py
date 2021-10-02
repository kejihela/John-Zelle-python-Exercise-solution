def main():
    print("This program will print your fine of a speed limit")
    speed_limit= int(input("Please input your speed limit "))
    clocked_speed= int(input("Please input your clocked speed "))
    penalty = 200
    fine = 50
    over_limit = 5
    if clocked_speed > 90:
        if clocked_speed > speed_limit:
            fine = penalty + fine + 5*(clocked_speed - speed_limit)
            print("your fine is ", fine)
        else:
            fine = penalty + fine
            print("your fine is ", fine)
    else:
        if clocked_speed <= speed_limit:
            print("the speed is legal")
        else:
            fine = fine + (clocked_speed - speed_limit)*5
            print ("your fine is ", fine)
main()
    
               
