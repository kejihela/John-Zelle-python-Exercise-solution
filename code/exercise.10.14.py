from graphics import * 
class Face:
    def __init__(self, window, center, size, width, height):
        w = width/2
        h = height/2
        self.x,self.y = center.getX(), center.getY()
        self.xmin, self.xmax = self.x-w, self.x+w
        self.ymin, self.ymax = self.y-h, self.y+h
        self.window = window
        self.size = size
        self.center = center
        eyeSize = 0.15 * self.size
        eyeOff = self.size/3.0
        mouthSize = 0.8*self.size
        mouthOff = self.size/2.0
        self.head = Circle(self.center, self.size)
        self.head.draw(window)
        self.leftEye = Circle(self.center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(self.center,eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        p1 = self.center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = self.center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(self.window)

    def smile(self):
        self.mouth.undraw()
        eyeSize = 0.15 * self.size
        eyeOff = self.size/3.0
        mouthSize = 0.8*self.size
        mouthOff = self.size/2.0
        self.leftEye.move(eyeOff-eyeOff, eyeOff*2)
        self.rightEye.move(eyeOff-eyeOff, eyeOff*2)
        p1 = self.center.clone()
        p2 = self.center.clone()
        p1.move(-mouthSize/2, -mouthOff)
        p2.move(mouthSize/2, -mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(self.window)
        
    def wink (self):
        self.rightEye.undraw()
        self.mouth.undraw()
        eyeSize = 0.15 * self.size
        eyeOff = self.size/3.0
        mouthSize = 0.8*self.size
        mouthOff = self.size/2.0
        d1 = self.center.clone()
        d2 = self.center.clone()
        d1.move((-mouthSize/4)+0.3, mouthOff-0.1)
        d2.move((mouthSize/4)+0.3, mouthOff-0.1)
        w = Line(d1,d2)
        w.draw(self.window)
        p1 = self.center.clone()
        p2 = self.center.clone()
        p1.move(-mouthSize/2, -mouthOff)
        p2.move(mouthSize/2, -mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(self.window)
        

    def shock(self):
        self.mouth.undraw()
        eyeSize = 0.15 * self.size
        eyeOff = self.size/3.0
        mouthSize = 0.8*self.size
        mouthOff = self.size/2.0
        self.mouth = Circle(self.center, eyeSize-0.05)
        self.mouth.move(-eyeOff+0.15, -eyeOff)
        self.mouth.draw(self.window)
         

    def button(self,center, height, width, label):
        w = width/2
        h = height/2
        x,y = center.getX(), center.getY()
        self.xmin, self.xmax = x-w, x+w
        self.ymin, self.ymax = y-h, y+h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.emoji = Rectangle(p1,p2).draw(self.window)
        self.emoji.setOutline("black")
        Text(Point(x,y),label).draw(self.window)

    def move(self):
        self.x*=0.1
        self.y*=0.1
        
        

def main():
        window = GraphWin("Facial Expression", 500,500, autoflush = False)
        window.setCoords(0,0,5,5)
        Line(Point(0, 1.1), Point(5,1.1)).draw(window)
    

        for x in range(0, 5, 1):
            Text(Point(x,0.9), str(x)).draw(window)
            Line(Point(x, 1), Point(x,1.1)).draw(window)
        face = Face(window, Point(2.5,3), 0.5, .5, 0.8,)
        while 0 < face.x < 5 or 0<face.y<5:
           face.move()
           update(50)

if __name__ == '__main__':
    main()
        
        
        
