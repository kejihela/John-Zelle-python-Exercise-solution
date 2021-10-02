from graphics import *
def main():
    win = GraphWin("bouncing ball", 500,500)
    win.setCoords(0.0, 0.0, 50, 50)
    rectangle=Rectangle(Point(1, 1),Point(20,20))
    rectangle.draw(win)
    dx = 1
    dy = 1
    for i in range(1000):
        circle= Circle(Point(dx, dy), 1)
        circle.setFill("yellow")
        circle.draw(win)
        if dy==20 and dx ==20:
            dy = dy*0
            dx = dx*0
            print(i)
            #dy=1
        else:
            dy = dy+1
            dx = dx+1
      
            
        update(30)
            
    
main()
    
