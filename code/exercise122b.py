import math
from exercise123 import Team
class VolleyBall:
    def __init__(self,probA,probB):
        self.TeamA = Team(probA)
        self.TeamB = Team(probB)
        self.server = self.TeamB
        

    def Rally(self):
        self.n = 0
        while not self.isOver():
            if self.n%5 != 0:
                if self.server.winServe():
                    self.server.incScore()
                else:
                    self.changeServer()
                    self.server.incScore()
                    self.changeServer()
            else:
                self.changeServer
            self.n = self.n + 1
                




    def isOver(self):
        a,b = self.getScore()
        return a == 25 or b ==25 and abs(a-b)>=2

    def getScore(self):
        return self.TeamA.getScore(), self.TeamB.getScore()

    def changeServer(self):
        if self.server == self.TeamA:
            self.server = self.TeamB
        else:
            self.server = self.TeamA
