from graphics import *
import math
sqrt = math.sqrt
def main():
    win = GraphWin("The interception of lines", 400,400)
    win.setCoords(-10.0, -10.0, 10.0, 10.0)
    rad_text = Text(Point(-1,8), "radius").draw(win)
    int_text = Text(Point(-1,6), "interception").draw(win)
    
    rad = Entry(Point(2,8), 5).draw(win)
    inter = Entry(Point(4, 6), 5).draw(win)

    win.getMouse()

    
    radius = float(rad.getText())
    intercept = float(inter.getText())

    win.getMouse()
    try:
        
        circle = Circle(Point(0,0), radius)
        circle.setOutline("black")
        circle.draw(win)
        line = Line(Point(-8, intercept), Point(8, intercept))
        line.setOutline("black")
        line.draw(win)

        x1 = sqrt(radius**2 - intercept**2)
        x2 = -sqrt(radius**2 - intercept**2)

        dot1 = Circle(Point(x1, intercept), 0.3)
        dot1.setFill("red")
        dot1.setOutline("red")
        dot1.draw(win)

        dot2 = Circle(Point(x2, intercept), 0.3)
        dot2.setFill("red")
        dot2.setOutline("red")
        dot2.draw(win)

        output1 = Text(Point(-1,-6), "").draw(win)
        output2 = Text(Point(-3,-6), "").draw(win)
        output1.setText(x1)
        output2.setText(x2)
    except ValueError:
        print("the lines do not intercept")
    
main()
    
