from graphics import *
def main():
    win = GraphWin("converting TEMPERATURE", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1,3), "Celcius temperature").draw(win)
    Text(Point(1,1), "ferenheit temperature").draw(win)

    input_text = Entry(Point(2.5,3), 5)
    input_text.setText("0.0")
    input_text.draw(win)
    output_text = Text(Point(2.25, 1), "")
    output_text.draw(win)

    button = Text(Point(1.5,2), "Convert it")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    win.getMouse()

    celcius = float(input_text.getText())
    ferenheit = (9/5)*celcius+32
    output_text.setText(round(ferenheit, 2))

    win.getMouse()
    button.setTest("Done!")
main()

    

    
    
    
