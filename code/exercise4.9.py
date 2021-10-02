from graphics import *
import math
def main():
    win = GraphWin("Rectangle program", 500, 500)
    win.setCoords(0.0, 0.0, 24.0, 32.0)

    point1 = win.getMouse().draw(win)
    x1 = point1.getX()
    y1 = point1.getY()
    point2 = win.getMouse().draw(win)
    x2 = point2.getX()
    y2 = point2.getY()

    rectangle = Rectangle(Point(x1, y1), Point(x2,y2))
    rectangle.draw(win)

    win.getMouse()

    length = y2 - y1
    width = x2 - x1
    area_value = length * width

    Text(Point(4, 28), "Area").draw(win)
    area =  Text(Point(10, 28), "").draw(win)
    area.setText(area_value)


    perimeter_value = 2*(length + width)
    Text(Point(4, 24), "Perimeter").draw(win)
    perimeter = Text(Point(10, 24), "").draw(win)
    perimeter.setText(perimeter_value)

main()

    
    
