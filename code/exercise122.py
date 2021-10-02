from exercise122b import VolleyBall
from exercise123 import Team

class Statistics:
    def __init__(self):
        self.winA = 0
        self.winB = 0
        self.shootA = 0
        self.shootB = 0

    def Result(self, Game):
        a, b = Game.getScore()
        if a > b:
            self.winA = self.winA + 1
            if b ==0:
                self.shootA = self.shootA + 1
        else:
            self.winB = self.winB + 1
            if a == 0:
                self.shootB = self.shootB + 1

    def printReport(self):
        n = self.winA + self.winB
        print("The total number of", n, "games was simulated")
        print("       Win  ""  Win%  ""  Shoot  ""  Shoot%  "  )
        print("--------------------------------------------")
        printLine("TeamA: ", self.winA, self.shootA, n)
        printLine("TeamB: ", self.winB, self.shootB, n)

def printLine(label, win, shoot, n):
        print("{0}     {1}     {2}    {3}    {4}".format(label, win, float(win/n), shoot, float(shoot/n)))

def getInput():
    a = float(input("please, input the probability for TeamA "))
    b = float(input("please, input the probability for TeamA "))
    n = int(input("please, How many games do you want to Simulate "))
    return a,b,n


def main():
    stats = Statistics()
    probA, probB, n = getInput()
    
    for i  in range(n):
        VB = VolleyBall(probA,probB)
        VB.Rally()
        stats.Result(VB)
    stats.printReport()

main()

                                               
               
        
        
