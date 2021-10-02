from math import sin, cos, radians

class projectile:
    def __init__(self, angle,velocity, height):
        self.xpos = 0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity* sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time*self.xvel
        yvel1 = self.yvel - time*9.8
        self.ypos = self.yvel + (yvel1+self.yvel)/2
        self.yvel = yvel1
    
    def getY(self):
        return self.ypos
    
    def getX(self):  
        return self.xpos
    
    def Result(self):
        print("the distance travelled by the cannonball is: ", self.xpos)
        
def getInput():
    print("please input the corresponding values")
    a= float(input("please input the angle it make with horizontal "))
    v= float(input("please input the initial velocity "))
    h= float(input("please input the height "))
    t= float(input("please input the time "))
    return a, v, h, t



def main():
    angle, velocity, height, time = getInput()
    cannonball = projectile(angle, velocity, height)
    while(cannonball.getY() >= 0):
        cannonball.update(time)
    cannonball.Result()
main()
        
        
    

    
    
    
    
    
        

        
        
        
