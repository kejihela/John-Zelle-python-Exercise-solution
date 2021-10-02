from graphics import *
def main():
    win = GraphWin("Graphics for principal and rate problem", 500,500)
    win.setCoords(0.0, 0.0, 5.0, 5.0)
    principal_text = Text(Point(2,3), "Principal")
    principal_text.draw(win)
    rate_text = Text(Point(2,4), "Rate")
    rate_text.draw(win)

    rectangle = Rectangle(Point(2.5, 1.5), Point(3.5, 2.5))
    rectangle.setFill("red")
    rectangle.draw(win)

    message=Text(Point(2.5,1),"CONVERTION IN PROGRESS")
    message.draw(win)

    button = Text(Point(3, 2), "Solve it")
    button.draw(win)

    output = Text(Point(4,4), "")
    output.draw(win)
  

    input_principal = Entry(Point(3,3), 5).draw(win)
    input_rate = Entry(Point(3,4), 5).draw(win)

    win.getMouse()

    principal = float(input_principal.getText())
    rate = float(input_rate.getText())

    principal = principal * (1+rate)

    output.setText(round(principal,2))
    message.setText("DONE!!!")

    win.getMouse()
    win.close()
    
main()
