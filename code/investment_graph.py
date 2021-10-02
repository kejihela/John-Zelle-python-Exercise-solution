from graphics import *
def main():
    print("This program is to display 10 years investment profit and graph")
    investment = int(input("please input your principal "))
    rate = float(input("Please input the rate of investment "))
    
    win = GraphWin("10 years investment meter", 320, 240)
    win.setBackground('white')
    Text(Point(20, 230), " 0.0K").draw(win)
    Text(Point(20, 180), " 2.5K").draw(win)
    Text(Point(20, 130), " 5.0K").draw(win)
    Text(Point(20,  80), " 7.5K").draw(win)
    Text(Point(20,  30), "10.0K").draw(win)
    
    height = investment * 0.02
    rect = Rectangle(Point(40,230), Point(65, 230-height))
    rect.setFill('green')
    rect.setWidth(2)
    rect.draw(win)
    for year in range(1, 11):
        investment = investment * (1 + rate)
        x11 = (year * 25) + 40
        height = investment * 0.02
        rect = Rectangle(Point(x11, 230), Point(x11+25, 230 - height))
        rect.setFill('green')
        rect.setWidth(2)
        rect.draw(win)

    input("press enter key to proceed")
    win.close()
main()
       
    

    
   


