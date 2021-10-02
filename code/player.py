from random import random
class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        
    def getScore(self):
        return self.score

    def winServe(self):
        return random() < self.prob
    

    
    def incScore(self):
        self.score = self.score + 1
        
