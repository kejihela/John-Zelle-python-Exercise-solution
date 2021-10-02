from graphics import *
from button import Button
from dieView import DieView
class GreedInterface:
    def __init__(self):
        win = GraphWin("Greedy Dice's Game", 600,500)
        win.setCoords(0,0,5,5)
        win.setBackground("green3")
        self.banner = Text(Point(2.5, 4.5), "Greedy Dice")
        self.banner.setFill("yellow2")
        self.banner.setStyle("bold")
        self.banner.setSize(15)
        self.banner.draw(win)
        self.win = win
        self.buttons = []
        b = Button(self.win, Point(2.5,2), 1, 0.5, "ROLL ALL")
        self.buttons.append(b)
        b = Button(self.win, Point(2.5,1.3), 0.5, 0.5, "PASS")
        self.buttons.append(b)
        b = Button(self.win, Point(4.5,.5), 0.5, 0.5, "QUIT")
        self.buttons.append(b)
        buttn = [(0.8,3),(1.4,3),(2,3),(2.6,3),(3.2,3),(3.8,3)]
        x = 0
        for cx,cy in buttn:
            x+=1
            label = ("die {0}".format(x))
            b = Button(self.win, Point(cx,cy), 0.5, 0.2, label)
            self.buttons.append(b)

        self.dice = []
        dice = [(0.8,3.5),(1.4,3.5),(2,3.5),(2.6,3.5),(3.2,3.5),(3.8,3.5)]
        for cx,cy in dice: 
            d = DieView(self.win, Point(cx,cy), 0.5)
            self.dice.append(d)

       

    
        

    



