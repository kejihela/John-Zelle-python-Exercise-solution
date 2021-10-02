from graphics import *
from shottracker import shotTracker
from inputdialog2 import InputDialog
from button import Button
from random import randrange
from target import Target
import time

def main():
    win = GraphWin("Connonball Animation", 640,480, autoflush = True)
    win.setCoords(-10, -10, 210, 155)
    x = randrange(1,200,5)
    
    target = Target(win, Point(x,5), 20, 10)
  

    Line(Point(-10, 0), Point(210,0)).draw(win)
  
    for x in range(0, 210, 50):
        Text(Point(x,-5), str(x)).draw(win)
        Line(Point(x, 0), Point(x,2)).draw(win)
        
    while True:
        
        angle, vel, height = 45, 40, 2
        inputwin = InputDialog(win,angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()

        if choice == "QUIT":
            win.close()
            break
        angle, velocity, height = inputwin.getValues()
        shot = shotTracker(win, angle, velocity, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1/40)
            update(50)
            if target.xmin<=shot.getX()<=target.xmax and target.ymin<=shot.getY()<=target.ymax:
                time.sleep(3)
                win.close()
main()


