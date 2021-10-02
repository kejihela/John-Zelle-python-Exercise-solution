import math
pi = math.pi
def ladder():
    print("these program is said to print the length of a ladder")
    height = float(input( "please input the height of the wall "))
    x = float(input( "please input the ladder degree to the floor in degree "))
    radians = (pi/180)*x
    degree = math.sin(radians)

    lenght = height/degree
    print("The length of the ladder is ", lenght)
ladder()
    
    
