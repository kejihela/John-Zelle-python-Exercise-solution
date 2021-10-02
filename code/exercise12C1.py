from exercise12C2 import Dice
class PokerApp:
    def __init__(self,interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.PlayRound()
        if self.money > 130:
            self.name = self.interface.HighScore()
            self.writeFile(self.name)
            self.interface.close()
        else:
            self.interface.close()

    def PlayRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        msg, score = self.dice.score()
        self.interface.showResult(msg, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.value())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            roll = roll +1
            self.dice.roll(toRoll)
            self.interface.setDice(self.dice.value())
            if roll < 3:
                toRoll = self.interface.chooseDice()
    
                
    def writeFile(self, name):
        self.High_score = []
        filename2 = "Highscore.txt"
        infile = open(filename2, "r")
        for line in infile.readlines():
            if line == "\n":
                continue
            else:
                self.High_score.append(line)
        filename = "Highscore.txt"
        outfile = open(filename, "w")
        if len(self.High_score) == 10:
            self.High_score.remove(self.High_score[0])
        self.High_score.append([self.money,self.name])
        for i in self.High_score:
            print("{0}".format(i),file = outfile)
        outfile.close()
                
            
            
