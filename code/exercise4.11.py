from graphics import *
import math
def house():
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
    #door
    house_frame = x2 - x1
    door_width = (1/5) * house_frame
    door_roof = win.getMouse()
    door_length = door_roof.getY()
    x3 = door_roof.getX()
    y3 = door_roof.getY()
    x_door = x3 - door_width
    door = Rectangle(Point(x_door,y1), Point(x3,y3))
    door.draw(win)
    #window
    window_width = door_width/2
    w_w = window_width/2
    window_centre = win.getMouse()
    x4 = window_centre.getX()
    y4 = window_centre.getY()
    window = Rectangle(Point(x4-w_w, y4-w_w), Point(x4+w_w, y4+w_w))
    window.draw(win)
    #roof
    roof_value1 = win.getMouse().draw(win)
    y6 = y2-y1
    roof_value3 = Point(x1, y1+y6) 
    roof = Polygon(roof_value1,roof_value3, point2  )
    roof.draw(win)

    win.getMouse()
    win.close()

    


house()
