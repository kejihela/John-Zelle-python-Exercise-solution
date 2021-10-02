from graphics import *
from button import Button
class Transfer:
    def __init__(self,win):
        self.win = win
        self.banner = Text(Point(3,3), "")
        self.banner.setStyle("bold")
        self.banner.setFill("black")
        self.banner.setSize(13)
        self.banner.draw(self.win)

    def cash(self):
        self.banner.setText("How much do you want to Transfer")
        bttn1 = Button(self.win,Point(3,1),0.7,0.5,"OK")
        bttn1.activate()
        amount = Text(Point(2,2), "Amount")
        amount = Entry(Point(3,2),6)
        amount.setText("0.000")
        amount.draw(self.win)
        pt = self.win.getMouse()
        a = float(amount.getText())
        if bttn1.clicked(pt):
            amount.undraw()
            self.banner.setText("")
            bttn1.undraw()
            return a , bttn1.getLabel()

    def insufficient(self):
        self.banner.setText("INSUFFICIENT BALANCE")
        self.win.getMouse()
        self.banner.setText("")
        
