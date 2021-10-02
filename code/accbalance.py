from graphics import *
from button import Button
class AccBalance:
    def __init__(self,win):
        self.win = win
        self.banner = Text(Point(3,3), "")
        self.banner.setStyle("bold")
        self.banner.setFill("black")
        self.banner.setSize(13)
        self.banner.draw(self.win)

    def Balance(self,x):
        self.banner.setText("YOUR ACCOUNT BALANCE IS " )
        text = Text(Point(3,2), str(x)).draw(self.win)
        bttn1 = Button(self.win,Point(3,1),0.7,0.5,"OK")
        bttn1.activate()
        pt = self.win.getMouse()
        if bttn1.clicked(pt):
            self.banner.setText("")
            text.undraw()
            bttn1.undraw()
            return bttn1.getLabel()

    
        
