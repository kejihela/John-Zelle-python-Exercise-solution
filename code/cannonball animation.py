from graphics import *

class shotTracker:
    __init__(self, win, angle, velocity, height):
        self.proj = projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker,setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)
    def update(self, dt):
    
        self.proj.update(self, dt)

        centre = self.marker.getCentre()
        dx = self.proj.getX() - centre.getX()
        dy = self.proj.getY() - centre.getY()
        self.marker.Move(dx, dy)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def undraw():
        self.marker.undraw(win)

          
    
            
        









def main():
    
