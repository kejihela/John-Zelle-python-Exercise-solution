from graphics import *
def main():
    win = GraphWin("circle changing position",500,500)
    shape = Rectangle(Point(50,50),Point(100,100))
    shape.setOutline("black")
    shape.setFill("blue")
    shape.draw(win)

    message = Text(Point(200,300), "hello!,see your result").draw(win)

    for i in range(3):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2 = Rectangle(Point(dx, dy), Point(dx+50, dy+50))
        shape2.setOutline("yellow")
        shape2.setFill("red")
        shape2.draw(win)
    message.setText("Click again to quit")
    win.getMouse()
    win.close()
main()
