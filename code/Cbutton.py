from graphics import *
class CButton:
    def __init__(self, win, center, radius, label):
        x = center.getX()
        y = center.getY()
        self.xback = x-radius
        self.xfront = x+radius
        self.yback = y-radius
        self.yfront = y+radius
        self.circle = Circle(Point(x,y), radius).draw(win)
        self.circle.setFill("red")
        self.circle.setOutline("black")
        self.label = Text(center,label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        return(self.active and self.xback <= p.getX() <= self.xfront and self.yback <= p.getY() <= self.yfront)
    
    def getLabel(self):
        return self.label.getText()
        

    def activate(self):
        self.label.setFill("black")
        self.circle.setWidth(1)
        self.active = True

    def deactivate(self):
        self.label.setFill("darkgrey")
        self.circle.setWidth(1)
        self.active = False
        

               
        
        
        
        
