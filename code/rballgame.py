from player import Player
class RBallGame:
    def __init__(self,probA,probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA

    def play(self):
        while not self.isOver():
            if self.server.winServe():
                self.server.incScore()
            else:
                self.changeServer()

    def isOver(self):
        a,b = self.getScore()
        return a==15 or b == 15 or (a == 7 and b == 0) or (b==7and a==0)

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

    def getScore(self):
        return self.playerA.getScore(), self.playerB.getScore()
            
            
