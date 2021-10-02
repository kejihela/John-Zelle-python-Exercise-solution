from graphics import *
def main():
    print("This program will print the investment graph")
    principal = float(input("Please input the amount to invest "))
    rate = float(input("Please input the rate for your investment "))
    win = GraphWin("The investment graph", 320,240)
    win.setCoords(-1.75, -200, 11.5, 10400)
    
    Text(Point(-1, 0),  "0.0k").draw(win)
    Text(Point(-1, 2500), "2.5k").draw(win)
    Text(Point(-1, 5000), "5.0k").draw(win)
    Text(Point(-1, 7500), "7.5k").draw(win)
    Text(Point(-1, 10000), "10.0k").draw(win)
    

    
    bar = Rectangle(Point(0,0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    for year in range(1, 11):
        principal = principal * (1+rate)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))                                
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("press enter key to proceed")
    win.close()
main()

        
                                          
                                          
        
    

