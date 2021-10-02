from rballgame import RBallGame
from player import Player
from random import random
class Stats:
    def __init__(self):
        self.winA = 0
        self.winB = 0
        self.shootA = 0
        self.shootB = 0

    def update(self, aGame):
        a, b = aGame.getScore()
        if a > b:
            self.winA = self.winA + 1
            if b == 0:
                self.shootA = self.shootA + 1
        else:
            self.winB = self.winB + 1
            if a==0:
                self.shootB = self.shootB + 1
    def printReport(self):
        n = self.winA + self.winB
        print (" Summary of" , n , " games: \ n" )
        print (" wins (% total ) shutout s (% wins ) " )
        print ("--------------------------------------------" )
        self.printLine ("A" , self.winA , self.shootA, n)
        self.printLine ("B" , self.winB , self.shootB, n)

    def printLine(self,label,wins,shuts,n):
        template = " Player {0} : {1:5} ({2:5.1%} ) {3:11}({4})"
        if wins == 0 : 
            shutStr = "-----"
        else :
            shutStr = "{0:4.1%}".format (float(shuts)/wins )

        print (template.format(label ,wins, float(wins)/n , shuts , shutStr))


def getInputs():
# Returns the three simulation parameters
    a = float(input("What is the prob player A wins a serve? " ) )
    b = float(input("What is the prob player B wins a serve? " ) )
    n = int(input("How many games to simulate? " ) )
    return a , b , n


def main():
   
    probA,probB, n = getInputs()
    sim = Stats()
   
    for i in range(n):
        rball = RBallGame(probA, probB)
        rball.play()
        sim.update(rball)


    sim.printReport()

if __name__ == '__main__':
    main()
        
        
    
