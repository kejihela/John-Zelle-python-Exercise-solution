from graphics import *
def triangle_2():
    win = GraphWin("Drawing triangle", 320,240)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5.0, 3.0), "please click anywhere 3 times")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1 , p2, p3)
    triangle.setOutline("cyan")
    triangle.setFill("yellow")
    triangle.draw(win)

    message.setText("click anywhere to exist")
    win.getMouse()

    

triangle_2()
