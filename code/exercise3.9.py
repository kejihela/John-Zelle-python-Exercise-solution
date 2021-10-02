import math
def area_triangle():
    print("This program is ready to print area of a triangle, pls feed me!")
    a = float(input("pls, input the value of a "))
    b = float(input("pls, input the value of a "))
    c = float(input("pls, input the value of a "))

    s = (a + b + c)/2
    a = s - a
    b = s - b
    c = s - c

    area = math.sqrt(s * a * b * c)
    print("The area of the triangle is", area)
area_triangle()
    
