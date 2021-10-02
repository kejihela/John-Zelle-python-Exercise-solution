from graphics import *
class Target:
    def __init__(self,win,center, width, height):
        self.win = win
        x = center.getX()
        y = center.getY()
        w = width/2
        h = height/2
        self.xmin, self.xmax = x-w, x+w
        self.ymin, self.ymax = y-h, y+h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("black")
        self.rect.draw(self.win)




        
        

        
        
