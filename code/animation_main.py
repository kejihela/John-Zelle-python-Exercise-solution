from graphics import *
from shottracker import shotTracker
from inputdialog2 import InputDialog
from button import Button
def main():
    win = GraphWin("connonball Animation", 640,480, autoflush = True)
    win.setCoords(-10, -10, 210, 155)

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
            break
        angle, velocity, height = inputwin.getValues()
        shot = shotTracker(win, angle, velocity, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1/50)
            update(50)
main()

