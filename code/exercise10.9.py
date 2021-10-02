from math import *
class sphere:
    def __init__(self,radius):
        self.radius = float(radius)

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4*pi*self.radius**2

    def volume(self):
        return (4/3)*(self.radius *pi)**3

def main():
    print("This program will calculate the properties of a sphere")
    r = input("please enter the value of your radius ")
    sphere1 = sphere(r)
    rad = sphere1.getRadius()
    are = sphere1.surfaceArea()
    vol = sphere1.volume()
    print("Radius: ",rad,"\nSurface Area: ",are,"\nVolume: ",vol)
if __name__ == '__main__':
    main()
    
    
