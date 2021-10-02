from graphics import *
from button import Button
class Introduction:
    def __init__(self):
        self.win = GraphWin("This print introduction", 600,400)
        text1 = "This is a Poker Game where you would be given"
        text2 = " certain sum of money to play click on"
        text3 = "let's play  and Exit to leave the window"
        
        introduction1 = Text(Point(300, 30), text1)
        introduction2 = Text(Point(300, 60), text2)
        introduction3= Text(Point(300, 90), text3)
        introduction1.setFill("yellow2")
        introduction1.setSize(16)
        introduction1.setStyle("bold")
        introduction1.draw(self.win)

        introduction2.setFill("yellow2")
        introduction2.setSize(16)
        introduction2.setStyle("bold")
        introduction2.draw(self.win)

        introduction3.setFill("yellow2")
        introduction3.setSize(16)
        introduction3.setStyle("bold")
        introduction3.draw(self.win)
        self.win.setBackground("green3")
        self.button = []
        b = Button(self.win , Point(100,300), 70, 70, "Let's Play")
        self.button.append(b)
        b = Button(self.win , Point(500,300), 70, 70, "Exit")
        self.button.append(b)

    def click(self):
        for b in self.button:
            b.activate()
        p = self.win.getMouse()
        while True:
            for b in self.button:
                if b.clicked(p):
                    if b.getLabel() == "Exit":
                        return self.win.close()
                    else:
                        return b.getLabel()
    def close(self):
        return self.win.close()

        
        

                            
