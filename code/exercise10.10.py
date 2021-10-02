from math import *
class cube:
    def __init__(self, perimeter):
        self.perimeter = float(perimeter)

    def getPerimeter(self):
        return self.perimeter

    def surfaceArea(self):
        return 6*(self.perimeter)**2

    def volume(self):
        return self.perimeter**3

def main():
    print("This program will calculate the properties of a sphere")
    p = input("please enter the value of your perimeter ")
    cube1 = cube(p)
    per = cube1.getPerimeter()
    are = cube1.surfaceArea()
    vol = cube1.volume()
    print("Perimeter: ",per,"\nSurface Area: ",are,"\nVolume: ",vol)
if __name__ == '__main__':
    main()
    
    
