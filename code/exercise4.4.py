from graphics import *

def main():
    win = GraphWin('winter',800,450)
    win.setBackground('darkgrey')
    snow = Rectangle(Point(0,170), Point(800,450))
    snow.setFill('white')
    snow.draw(win)

    tree = Polygon(Point(60,300), Point(120,50), Point(180,300))
    tree.setFill('green')
    tree.draw(win)

    tree = Polygon(Point(200,200), Point(230,70), Point(260,200))
    tree.setFill('green')
    tree.draw(win)

    tree = Polygon(Point(500,300), Point(550,40), Point(600,300))
    tree.setFill('green')
    tree.draw(win)

    tree = Polygon(Point(600,350), Point(670,50), Point(740,350))
    tree.setFill('green')
    tree.draw(win)

    circle = Circle(Point(400,300),80)
    circle.setFill('white')
    circle.draw(win)

    circle = Circle(Point(400,210),50)
    circle.setFill('white')
    circle.draw(win)

    circle= Circle(Point(400,145),30)
    circle.setFill('white')
    circle.draw(win)

    coal = Circle(Point(390,140),5)
    coal.setFill('black')
    coal.draw(win)

    coal = Circle(Point(410,140),5)
    coal.setFill('black')
    coal.draw(win)

    coal = Circle(Point(386,158),4)
    coal.setFill('black')
    coal.draw(win)

    coal = Circle(Point(400,163),4)
    coal.setFill('black')
    coal.draw(win)

    coal = Circle(Point(414,158),4)
    coal.setFill('black')
    coal.draw(win)


    win.getMouse() # pause for click in window
    win.close()

main()
        
