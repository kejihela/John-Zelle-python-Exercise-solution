from graphics import *
from button import Button

class DrawFace:
    def __init__(self, centre, size):
        self.win = GraphWin("face", 500, 500)
        self.win.setCoords(0, 0, 5, 5)
        self.head = Circle((centre), size).draw(self.win)
        self.head.setOutline("black")
        self.head.setFill("white")
        self.eye_ball = (size*0.05)/size

    def eye(self, x, y):
        self.eye1 = Circle(Point(x-0.2, y+0.2), self.eye_ball).draw(self.win)
        self.eye2 = Circle(Point(x+0.25, y+0.2), self.eye_ball).draw(self.win)
        self.eye1.setFill("black")
        self.eye2.setFill("black")
        
    def nose(self, x,y):
        self.rect1 = Rectangle(Point(x-0.1, y-0.1),Point(x,y)).draw(self.win)
        self.rect2 = Rectangle(Point(x+0.1, y-0.1),Point(x,y)).draw(self.win)
        self.rect1.setFill("black")
        self.rect2.setFill("black")

    def mouth(self,x,y):
        self.mouth = Rectangle(Point(x-0.1, y-0.25),Point(x+0.1,y-0.25)).draw(self.win)
        self.mouth.setFill("black")
        
    

    

def main():
    win = GraphWin("face", 500, 500)
    win.setCoords(0, 0, 5, 5)
    

    
    while True:
        draw = Button(win, Point(1,4.5), 1.25, .5, "DRAW")
        draw.activate()
         
        Quit = Button(win, Point(1,3.5), 1.25, .5, "QUIT")
        Quit.activate()

        pt = win.getMouse()
        if Quit.clicked(pt):
            win.close()
            break
        draw.clicked(pt)
        
        face = DrawFace(Point(2,3), 0.5)
        face.eye(2,3)
        face.nose(2,3)
        face.mouth(2,3)

        pt = win.getMouse()

main()
    
        

        
        


