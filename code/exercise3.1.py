import math
pi = math.pi
def sphere():
    print("This program would print the surface area and volume of a sphere")
    radius = float(input("input your radius "))
    sphere_area = 4 * pi * (radius**2)
    sphere_volume = (4/3) * pi * radius**3
    print(sphere_area)
    print(sphere_volume)
sphere()
