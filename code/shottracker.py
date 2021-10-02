from graphics import *
from cannonball2 import projectile


class shotTracker:
    def __init__(self, win, angle, velocity, height):
        self.proj = projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)
        
    def update(self, dt):
    
        self.proj.update(dt)

        centre = self.marker.getCenter()
        dx = self.proj.getX() - centre.getX()
        dy = self.proj.getY() - centre.getY()
        self.marker.move(dx, dy)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def undraw():
        self.marker.undraw(win)

          
    

    
