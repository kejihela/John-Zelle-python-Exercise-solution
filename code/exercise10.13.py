from graphics import * 
class Face:
    def __init__(self, window, center, size, width, height):
        w = width/2
        h = height/2
        x,y = center.getX(), center.getY()
        self.xmin, self.xmax = x-w, x+w
        self.ymin, self.ymax = y-h, y+h
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
        

def main():
        window = GraphWin("Facial Expression", 500,500)
        window.setCoords(0,0,5,5)
        face = Face(window, Point(2.5,3), 0.5, .5, 0.8,)
        face.button(Point(2.5,1), .5, 0.8, "EMOJI")
        pt= window.getMouse()
        if face.xmin<=pt.getX()<=face.xmax and face.ymin<=pt.getY()<=face.ymax:
            face.smile()
            pt = window.getMouse()
            if face.xmin<=pt.getX()<=face.xmax and face.ymin<=pt.getY()<=face.ymax:
                face.shock()
                pt = window.getMouse()
                if face.xmin<=pt.getX()<=face.xmax and face.ymin<=pt.getY()<=face.ymax:
                    face.wink()
        pt =  window.getMouse()
        if face.xmin<=pt.getX()<=face.xmax and face.ymin<=pt.getY()<=face.ymax:
            window.close()
               

if __name__ == '__main__':
    main()
        
        
        
