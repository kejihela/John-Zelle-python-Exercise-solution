from graphics import *
from random import randrange
class newDieView:
    def __init__(self, win, center,  size):
        self.win = win
        cx = center.getX()
        cy = center.getY()
        d_size = size/2
        xmin = cx-d_size
        ymin = cy-d_size
        xmax = cx+d_size
        ymax = cy+d_size
        p1=Point(xmin, ymin)
        p2= Point(xmax, ymax)
        dice = Rectangle(p1,p2)
        dice.draw(self.win)
        dice.setFill("white")
        self.psize = 0.1*size
        offset = 0.6*d_size
        self.background = "white"
        self.foreground = "black"
        self.variable=0

        self.pip1 = self.__makepip(cx-offset, cy-offset)
        self.pip2 = self.__makepip(cx-offset, cy)
        self.pip3 = self.__makepip(cx-offset, cy+offset)
        self.pip4 = self.__makepip(cx, cy)
        self.pip5 = self.__makepip(cx+offset, cy-offset)
        self.pip6 = self.__makepip(cx+offset, cy)
        self.pip7 = self.__makepip(cx+offset, cy+offset)

        self.setValue(1)
         
    def __makepip(self, x,y):
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setColor(self, color):
        self.foreground = color
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        if self.variable  == 1:
            self.pip4.setFill(self.foreground)
        elif self.variable ==2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif self.variable  ==3:
            self.pip1.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif self.variable ==4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif self.variable ==5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
         
    
    def setValue(self,value):
        self.variable = value
        self.foreground = "black"
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        self.variable = value
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value==2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value ==3:
            self.pip1.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value ==4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value==5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            
        
        
