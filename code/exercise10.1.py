from math import sin, cos, radians
class cannonball:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        self.max = (velocity* velocity) * (sin(theta))**2

    def update(self, time):
        self.xpos = self.xpos + time*self.xvel
        yvel1 = self.yvel - time*9.8
        self.ypos = self.ypos + time*(yvel1 + self.yvel)/2
        self.yvel = yvel1

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos


    def getMaxheight(self):
        self.s = self.max/(2*9.8)
        return self.s

def getInput():
    a = float(input("please input your angle "))
    v = float(input("please input your velocity "))
    h = float(input("please input your height "))
    t = float(input("please input your time "))
    return a, v, h,t


def main():
    angle, velocity, height, time = getInput()
    cb1 = cannonball(angle, velocity, height)
    while cb1.getY() >= 0:
        cb1.update(time)
    

    print("\nDistance traveled: {0:0.1f} meters.".format(cb1.getX()))
    print("\nmaximum height reached ",cb1.getMaxheight())
    

main()
    

    
        
