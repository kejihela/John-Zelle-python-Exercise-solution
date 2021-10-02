from graphics import *
def main():
    win =GraphWin()
    shape = Circle(Point(50,50), 30)
    shape.setOutline("red")
    shape.setFill("blue")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()
main()
        
        
