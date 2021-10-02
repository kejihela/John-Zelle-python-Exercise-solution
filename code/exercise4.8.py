import math
from graphics import *
def main():
    win = GraphWin("This is a line segment program", 320,240)
    win.setCoords(0.0, 0.0, 24, 32)
    point1 = win.getMouse().draw(win)
    point2 = win.getMouse().draw(win)
   
    x1 = point1.getX()
    y1 = point1.getY()
    x2 = point2.getX()
    y2 = point2.getY()

    mid_value1 = (x1 + x2)/2
    mid_value2 = (y1 + y2)/2
    mid_point = Circle(Point(mid_value1, mid_value2), 0.2)
    mid_point.setFill("cyan")
    mid_point.draw(win)
    
    win.getMouse()
    
    line = Line(Point(x1, y1), Point(x2,y2))
    line.draw(win)

    dx = x2 - x1
    dy = y2 - y1
    slope_value = dy/dx
    length_value = math.sqrt(dx**2 + dy**2)
    
    slope = Text(Point(12, 25), "").draw(win)
    Text(Point(3, 25), "Slope").draw(win)
    slope.setText(slope_value)

    length = Text(Point(12, 30), "").draw(win)
    Text(Point(4, 30), "Length").draw(win)
    length.setText(length_value)
    
main()
