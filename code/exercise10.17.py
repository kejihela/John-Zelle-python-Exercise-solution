from graphics import *
class Regression:
    def __init__(self,win,centre,height,width,label):
        self.win = win
        self.m =0
        self.x = 0
        self.y = 0
        self.xy = 0
        self.n = 0
        self.x_sqr = 0
        w = width/2
        h = height/2
        x = centre.getX()
        y = centre.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax,self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.draw(self.win)
        self.label = Text(centre, label)
        self.label.draw(self.win)
        
    def Addpoint(self, pt):
        self.n = self.n + 1
        a = pt.getX()
        b = pt.getY()
        self.x = self.x + a
        self.y = self.y + b
        self.xy = self.xy + (self.x*self.y)
        self.x_bar = self.x/self.n
        self.y_bar = self.y/self.n
        self.x_sqr = self.x_sqr + (self.x**2)
        self.x_bar_sqr = self.x_bar**2
        
          
    def draw(self):
        self.m = (self.xy - (self.n*self.x_bar*self.y_bar))/(self.x_sqr - (self.n*self.x_bar_sqr))
        y_line1 = self.y_bar + self.m *(0 - self.x_bar)
        y_line2 = self.y_bar + self.m *(5- self.x_bar)
        regression_line = Line(Point(0, y_line1), Point(5,y_line2)).draw(self.win)

def main():
    win = GraphWin("Regression Line", 500,500)
    win.setCoords(0.0,0.0,5.0,5.0)
    reg = Regression(win,Point(4,0.5),0.5,0.5,"Done")
    pt = win.getMouse().draw(win)
    while True:
        reg.Addpoint(pt)
        pt = win.getMouse().draw(win)
        if reg.xmin<=pt.getX()<=reg.xmax and reg.ymin<=pt.getY()<=reg.ymax:
            reg.draw()
            win.getMouse()
            win.close()
    

main()
