from graphics import *
from random import randrange

class Door:
    def __init__(self, win, center, height, width, label):
        w = width/2
        h = height/2
        x,y = center.getX(), center.getY()
        self.xmin, self.xmax = x-w, x+w
        self.ymin, self.ymax = y-h, y+h
        
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.door = Rectangle(p1,p2).draw(win)
        self.door.setOutline("black")
        Text(Point(x,y),label).draw(win)
        
        
    
def cpu_select():
    select = randrange(1,4)
    if select ==1:
        return "DOOR 1"
    elif select ==2:
        return "DOOR 2"
    else:
        return "DOOR 3"
        

def main():
    win = GraphWin("DOORS", 500, 500)
    win.setCoords(0, 0, 4, 4)
    door1 = Door(win, Point(1,2), .5, 0.8, "DOOR 1")
    door2 = Door(win, Point(2,2), .5, 0.8, "DOOR 2")
    door3 = Door(win, Point(3,2), .5, 0.8, "DOOR 3")
    select = cpu_select()
    prompt = Text(Point(2,3.5),"Please, click one of the button").draw(win)
    pt = win.getMouse()
    prompt.undraw()
    if door1.xmin<=pt.getX()<=door1.xmax and door1.ymin<=pt.getY()<=door1.ymax:
        if select == "DOOR 1":
            Text(Point(2,3.5),"You won,you selected DOOR 1 and computer also selects DOOR 1").draw(win)
        else:
            Text(Point(2,3.5),"You lose computer select").draw(win)
            Text(Point(2,3.5),select).draw(win)
            
    elif door2.xmin<=pt.getX()<=door2.xmax and door2.ymin<=pt.getY()<=door2.ymax:
        if select == "DOOR 2":
            Text(Point(2,3.5),"You won,you selected DOOR 2 and computer also selects DOOR 2").draw(win)
    
        else:
            Text(Point(2,3.5),"You lose computer select").draw(win)
            Text(Point(2,3),select).draw(win)    
            
    elif door3.xmin<=pt.getX()<=door3.xmax and door3.ymin<=pt.getY()<=door3.ymax:
        if select == "DOOR 3":
            Text(Point(2,3.5),"You won,you selected DOOR 3 and computer also selects DOOR 3").draw(win)
        else:
            Text(Point(2,3.5),"You lose computer select").draw(win)
            Text(Point(2,3),select).draw(win)
            
    
main()
