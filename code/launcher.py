from graphics import *
from math import cos,sin,radians
from shottracker import shotTracker
class Launcher:

    def __init__(self, win):
        Base = Circle(Point(0,0), 3)
        Base.setFill("red")
        Base.setOutline("red")
        Base.draw(win)

        self.win = win
        self.vel = 40
        self.angle = 45
        self.arrow = Line(Point(0,0),Point(0,0))
        self.arrow.draw(self.win)

        self.redraw()
        
    def adjAngle(self, amt):
        self.angle = self.angle + radians(amt)
        self.redraw()

    def adjVel(self, amt):
        self.vel = self.vel + amt
        self.redraw()

    def redraw(self):
        self.arrow.undraw()
        pt2 = Point(self.vel*cos(self.angle),self.vel*sin(self.angle))
        self.arrow = Line(Point(0,0), pt2).draw(self.win)
        self.arrow.setArrow("last")
        self.arrow.setWidth(3)

    def fire(self):
        return shotTracker(self.win, self.angle,self.vel,0.0)
        
        
