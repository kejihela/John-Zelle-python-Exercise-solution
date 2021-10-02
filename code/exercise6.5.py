import math
pi = math.pi
def area_pizza(radius):
    area = pi * radius**2
    return area
def cost(area, price):
    cost_per_sq = area/price
    return cost_per_sq
def main():
    print("This program will print the cost per square inch of circular pizza")
    radius = float(input("please input your value for radius "))
    price = float(input("please input your price for pizza "))
    areaOfPizza = area_pizza(radius)
    print(areaOfPizza)
    costPerSq = cost(areaOfPizza, price)
    print(costPerSq)
main()
