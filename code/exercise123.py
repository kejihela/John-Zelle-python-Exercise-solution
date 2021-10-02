from random import random
class Team:
    def __init__(self,prob):
        self.prob = prob
        self.score = 0

    def incScore(self):
        self.score = self.score + 1

    def getScore(self):
        return self.score

    def winServe(self):
        return random() < self.prob
