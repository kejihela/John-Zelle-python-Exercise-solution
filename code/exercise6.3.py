import math
pi = math.pi
def sphereArea(radius):
    sphere_area = 4 * pi * radius * radius
    return sphere_area
    
def sphereVolume(radius):
    sphere_volume = (4/3)*pi*radius**3
    return sphere_volume
def main():
     print("This program would print the surface area and volume of a sphere")
     radius = float(input("please input your radius "))
     area = sphereArea(radius)
     volume = sphereVolume(radius)
     print(area)
     print(volume)
main()
