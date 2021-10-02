class PokerApp:
    def __init__(self,interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            RoundPlay()
        self.interface.close()

    def RoundPlay(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        doRolls()
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
            self.roll(toRoll)
            self.interface.setDice(self.dice.value())
            if roll < 3:
                toRoll = self.interface.chooseDice()
                
            
            
