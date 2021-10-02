from dieView import DieView
from graphics import *
from button import Button
class GuiInterface:
    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300,30), "Python Poker Game")
        banner.setFill("yellow")
        banner.setSize(24)
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300,100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300, 170), 75, 30)
        b = Button(self.win, Point(300,230), 150, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        b = Button(self.win, Point(30,375), 40, 30, "Help")
        self.buttons.append(b)
        self.money = Text(Point(300,325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def choose(self, choices):
        buttons = self.buttons
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()
    
        

    def createDice(self, center, size):
        center.move(-3*size,0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range(1,6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            
            self.buttons.append(b)
            center.move(1.5*width, 0)
    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}, You win ${1}".format(msg,score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)
    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"
    def chooseDice(self):
        choices = []
        while True:
            b = self.choose(["Die 1","Die 2","Die 3","Die 4","Die 5", "Roll Dice", "Score", "Help"])
            if b[0] == "D":
                i = int(b[4]) - 1
                if i in choices:
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("grey")
            elif b[0] == "H":
                self.Help()
                
            else:
                for d in self.dice:
                    d.setColor("black")
                if b == "Score":
                    return []
                elif choices != []:
                    return choices
    
    def Help(self):
        texts = []
        window = GraphWin("HELP", 600, 400)
        window.setBackground("green3")
        text = "you will be given $100 to play, each game cost $10."
        texts.append(text)
        text = "you get the following score for coresponding values"
        texts.append(text)
        text = "Two Pairs $5, meaning having 2 same dice with 2 different values "
        texts.append(text)
        text = "Three of a Kind $8, having 3 dice of the same value "
        texts.append(text)
        text = "Full House A Pair and a Three of a Kind $12"
        texts.append(text)
        text = "Four of a Kind $ 15, having four dice of the same value"
        texts.append(text)
        text = "Straight (1-5 or 2-6) $ 20, having numbers from 1-5 0r 2-6"
        texts.append(text)
        text = "Five of a Kind $ 30, having five dice of the same value"
        texts.append(text)
        a = 30
        for i in texts:
            introduction = Text(Point(300, a), i)
            introduction.setFill("yellow2")
            introduction.setSize(12)
            introduction.setStyle("bold")
            introduction.draw(window)
            self.win.setBackground("green3")
            a = a + 30
            
            
            
        
            
    def close(self):
        self.win.close()

        
                        
                           
    
        
