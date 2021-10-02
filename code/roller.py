from random import randrange
from graphics import *
from Cbutton import CButton
from newdieview import newDieView

def main():
    print("This program is for rolling dice")
    win = GraphWin("Rolling Dice")
    win.setCoords(0,0,10,10)
    win.setBackground("green2")
    
    die1 = newDieView(win, Point(3,7), 2)
    die2 = newDieView(win, Point(7,7), 2)

    Roll_button = CButton(win, Point(2.5, 2.5), 1, "Roll")
    Quit_button = CButton(win, Point(7.5, 2.5), 1, "Quit")
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
            die1.setColor(color_rgb(255,0,0))
            die2.setColor(color_rgb(255,0,0))
        pt = win.getMouse()

    win.close()
main()
        
    
