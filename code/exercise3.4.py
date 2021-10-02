def thunder_strike():
    print("print the distance of a lightning strike")
    time = float(input("input the time between the sound and flash of the thunder in seconds "))
    speed = 1100 
    distance = speed * time
    distance = distance/5280
    print("the distance of the ligtning strike is", distance , "miles")
thunder_strike()
    
