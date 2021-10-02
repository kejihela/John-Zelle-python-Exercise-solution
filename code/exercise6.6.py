from graphics import *
import math
def distance(p1, p2):
    point_distance = math.sqrt((p2.getX()-p1.getX())**2 + (p2.getY()-p1.getY())**2)
    return point_distance
def perimeter(p1,p2,p3):
    perimeter = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    return perimeter
def area(p1,p2,p3):
    a = distance(p1,p2)
    b = distance(p2,p3)
    c = distance(p3,p1)
    s = (a+b+c)/2
    x = s-a
    y = s-b
    z = s-c
    area = math.sqrt(s*x*y*z)
    return area

def main():
    print("This program is ready to print area of a triangle, pls feed me!")
    win = GraphWin("Area and Perimeter", 500,500)
    
    p1 =win.getMouse()
    p1.draw(win)
    p2 =win.getMouse()
    p2.draw(win)
    p3 =win.getMouse()
    p3.draw(win)
    Polygon(p1,p2,p3).draw(win)

    win.getMouse()
    distance(p1, p2)
    perimeterTriangle = perimeter(p1,p2,p3)
    areaTriangle = area(p1,p2,p3)
    print(perimeterTriangle)
    print(areaTriangle)
   
  
main()
    
    
