from graphics import *
def label():
    window=GraphWin("investment and interest", 500,500)
    window.setCoords(-3.0, -1000.0, 11.4, 11000.0 )
    Text(Point(-1, -500), "0.0k").draw(window)
    Text(Point(-1, 2500), "2.5k").draw(window)
    Text(Point(-1, 5000), "5.0k").draw(window)
    Text(Point(-1, 7500), "7.5k").draw(window)
    Text(Point(-1, 10000), "10.0k").draw(window)
    return window

def drawbar(win, year, principal): 
    bar = Rectangle(Point(year, -500), Point(year+1, principal))
    bar.setWidth(2)
    bar.setFill("green")
    bar.draw(win)

def main():
    print("This program is to print the future value problem")
    principal=float(input("please input your principal "))
    rate = float(input("please input your rate "))
    
    win = label()

    drawbar(win, 0 , principal)

    for year in range(1, 11):
        principal = principal * (1+rate)
        drawbar(win, year , principal)

    
        

main()

    
                    
