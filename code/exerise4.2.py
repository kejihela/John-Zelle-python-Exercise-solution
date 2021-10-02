from graphics import *
def main():
    win = GraphWin("Archery Target", 500, 500)
    circle = Circle(Point(250, 250), 50)
    circle.setFill("white")
    circle.setOutline("black")
    circle.draw(win)

    circle = Circle(Point(250, 250), 40)
    circle.setFill("black")
    circle.setOutline("black")
    circle.draw(win)

    circle = Circle(Point(250, 250), 30)
    circle.setFill("blue")
    circle.setOutline("black")
    circle.draw(win)

    circle = Circle(Point(250, 250), 20)
    circle.setFill("red")
    circle.setOutline("black")
    circle.draw(win)
    
    circle = Circle(Point(250, 250), 10)
    circle.setFill("yellow")
    circle.setOutline("black")
    circle.draw(win)
  

main()
         
