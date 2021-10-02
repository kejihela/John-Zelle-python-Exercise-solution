from graphics import *
def main():
    print("draw a regression line")
    win = GraphWin("draw a regression line", 500,500)
    win.setCoords(0.0,0.0,5.0,5.0)
    Text(Point(2.7, 1.2), "Done!").draw(win)
    X = 0
    Y = 0
    n = 1
    sqX = 0
    sqY = 0
    text = Rectangle(Point(2,1), Point(3.5,1.5)).draw(win)
    p = win.getMouse().draw(win)
    while p.getX() >=2  and p.getY()>=1.5:
        n =  n + 1 
        x = p.getX()
        y = p.getY()
        X = X + x
        Y = Y + y
        sqX = sqX + (X**2)
        xy  = X * Y
        p = win.getMouse().draw(win)
    X_bar = X/n
    Y_bar = Y/n

    m = (xy - (n*X_bar*Y_bar))/(sqX - n*X_bar*X_bar)
    y_line1 = Y_bar + m*(0 - X_bar)
    y_line2 = Y_bar + m*(5- X_bar)

    regression_line = Line(Point(0, y_line1), Point(5,y_line2)).draw(win)
    win.getMouse()
    win.close()
         
        
    print("X",X,"sqX",sqX) 
    print("Y",Y)
    print("xy",xy)
    print("m",m)
    print(y_line1,y_line2)
        
       
main()
    
