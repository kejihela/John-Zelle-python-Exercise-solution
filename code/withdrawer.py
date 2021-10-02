from ATMinterface import Interface
import time
from button import Button
from graphics import *
class Withdraw:
    def __init__(self,win):
        self.win = win
        self.banner = Text(Point(3,3.5), "")
        self.banner.setStyle("bold")
        self.banner.setFill("black")
        self.banner.setSize(13)
        self.banner.draw(self.win)
        self.bttn_list = [(-0.5,3),(-0.5,2),(-0.5,1),(5.5,3),(5.5,2),(5.5,1)]


    def cash(self):
        self.banner.setText("How much do you want to withdraw")
        label = 2000
        bttn = []
        for (cx,cy) in self.bttn_list:
            label = label + 1000
            b = Button(self.win,Point(cx,cy),0.5,0.5,str(label))
            b.activate()
            bttn.append(b)
        pt = self.win.getMouse()
        for b in bttn:
            b.undraw()
        for b in bttn:
            self.banner.setText("")
            if b.clicked(pt):
                return b.getLabel()

        
        

        
        

    
        

    
        
