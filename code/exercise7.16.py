from graphics import *
def main():
    win = GraphWin("this is a game", 500,500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    circle1 = Circle(Point(5,5), 2.5)
    circle1.setFill("white")
    circle1.draw(win)

    circle2 = Circle(Point(5,5), 2.0)
    circle2.setFill("black")
    circle2.draw(win)

    circle3 = Circle(Point(5,5), 1.5)
    circle3.setFill("blue")
    circle3.draw(win)

    circle4 = Circle(Point(5,5), 1.0)
    circle4.setFill("red")
    circle4.draw(win)

    circle5 = Circle(Point(5,5), 0.5)
    circle5.setFill("yellow")
    circle5.draw(win)
    total = 0
    for i in range(5):    
        point = win.getMouse()
        x1=point.getX()
        y1=point.getY()
        if x1 >= 4.5 and x1<=5.5 and y1 >= 4.5 and y1<=5.5:
            total = total + 9
        elif x1>=4.0 and x1<=6.0 and y1 > 4.0 and y1<=6.0:
            total = total+7         
        elif x1 > 3.5 and x1<=6.5 and y1 > 3.5 and y1<=6.5:
              total = total +5
        elif x1 >3.0 and x1<=7.0 and y1 > 3.0 and y1<=7.0:
              total = total +3
        elif x1 > 2.5 and x1<=7.5 and y1 > 2.5 and y1<=7.5:
              total = total +1
        else:
              total = total +0

        print(total)
           
    
main()
    
    
