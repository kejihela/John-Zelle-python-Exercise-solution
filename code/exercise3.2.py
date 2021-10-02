import math
pi = math.pi
def circular_pizza():
    print("This program will print the cost per square inch of a circular pizza")
    price = float(input("what's the price of the pizza "))
    diameter = float(input("what's the diameter of the pizza "))
    radius = diameter / 2
    area = pi * radius**2
    ans = area/price
    print("The cost per square inch of the circular pizza is ", ans)
circular_pizza()
