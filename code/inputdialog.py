from graphics import *
from button import Button

class InputDialog:
    def __init__(self,win, angle, velocity, height):
        self.win = win

        #self.win = win =GraphWin("Input Dialog", 300,300)
        #win.setCoords(0, 4.5, 4, 0.5)

        Text(Point(1,1), "Angle").draw(self.win)
        self.angle = Entry(Point(3,1), 5).draw(self.win)
        self.angle.setText(str(angle))

        Text(Point(1,2), "Velocity").draw(self.win)
        self.velocity = Entry(Point(3,2), 5).draw(self.win)
        self.velocity.setText(str(velocity))

        Text(Point(1,3), "Height").draw(win)
        self.height = Entry(Point(3,3), 5).draw(self.win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(3,3.5), 1.25, .5, "Fire!")
        self.fire.activate()
        
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    def interact(self):
        while True:
        
            pt = self.win.getMouse()
        
            if self.fire.clicked(pt):
                return "FIRE"

            if self.quit.clicked(pt):
                return "QUIT"

    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.velocity.getText())
        h = float(self.height.getText())
        return a,v,h

    def close(self):
        self.win.close()

   
    

        
