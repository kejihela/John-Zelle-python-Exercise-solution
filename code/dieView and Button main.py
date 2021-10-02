from random import randrange
from graphics import GraphWin, Point
from button import Button
from dieView import DieView

def main():
    print("This program is for rolling dice")
    win = GraphWin("Rolling Dice")
    win.setCoords(0,0,10,10)
    win.setBackground("green2")
    
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7,7), 2)

    Roll_button = Button(win, Point(5, 4.5), 6, 1, "Roll_Dice")
    Quit_button = Button(win, Point(5, 1), 6, 1, "Quit")
    Roll_button.activate()
    
    pt = win.getMouse()
    while not Quit_button.clicked(pt):
        if Roll_button.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setValue(value2)
            Quit_button.activate()
        pt = win.getMouse()

    win.close()
main()
        
    
