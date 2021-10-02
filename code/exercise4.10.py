from graphics import *
import math
def main():
    win = GraphWin("Triangle program", 500, 500)
    win.setCoords(0.0, 0.0, 24.0, 32.0)

    point1 = win.getMouse().draw(win)
    x1 = point1.getX()
    y1 = point1.getY()
    point2 = win.getMouse().draw(win)
    x2 = point2.getX()
    y2 = point2.getY()
    point3 = win.getMouse().draw(win)
    x3 = point3.getX()
    y3 = point3.getY()

    triangle = Polygon(point1, point2, point3)
    triangle.draw(win)

    win.getMouse()

    length1 = y1 - y2
    length2 = x3 - x2
    length3 = y1 - y3

    s = (length1 + length2 + length3)/2
    area_value = math.sqrt(s*((s- length1) * (s-length2) * (s-length3)))
    Text(Point(4, 28), "Area").draw(win)
    area =  Text(Point(10, 28), "").draw(win)
    area.setText(area_value)


    perimeter_value = (length1) + (length2) + (length3)
    Text(Point(4, 24), "Perimeter").draw(win)
    perimeter = Text(Point(10, 24), "").draw(win)
    perimeter.setText(perimeter_value)

main()
