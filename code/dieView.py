"""this is a program of dieView"""
from graphics import *
class DieView:
    def __init__(self, win, centre, size):
        self.win = win
        self.background = 'white'
        self.foreground = 'black'
        hsize = size/2
        self.psize = 0.1 * size
        offset = 0.6 * hsize
        cx = centre.getX()
        cy = centre.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(self.win)
        rect.setFill(self.background)
        

        self.pip1 = self.__makepip(cx-offset, cy-offset)
        self.pip2 = self.__makepip(cx-offset, cy)
        self.pip3 = self.__makepip(cx-offset, cy+offset)
        self.pip4 = self.__makepip(cx, cy)
        self.pip5 = self.__makepip(cx+offset, cy-offset)
        self.pip6 = self.__makepip(cx+offset, cy)
        self.pip7 = self.__makepip(cx+offset, cy+offset)

        self.setValue(1)

    def __makepip(self, x,y):
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        self.value = value
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        if value==1:
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
            
    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)            
            
            
            
    

    
        
        
        
        
