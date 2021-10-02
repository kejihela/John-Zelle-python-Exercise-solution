import math
def distance_btw_2points():
    print("The program is design to calculate for the distance between 2 points")
    x1 = float(input("Please input the value of x1 "))
    x2 = float(input("Please input the value of x2 "))
    y1 = float(input("Please input the value of y1 "))
    y2 = float(input("Please input the value of y2 "))
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    distance = math.sqrt(x + y)
    print("The distance between the line is ", distance)
distance_btw_2points()
