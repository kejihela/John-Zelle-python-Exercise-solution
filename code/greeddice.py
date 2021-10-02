from random import randrange
class Dice:
    def __init__(self):
        self.dice = [0]*5
        self.rollAll()

    def roll(self,lst):
        for x in lst:
            self.dice[x] = randrange(1,7)
        return self.dice

    def rollAll(self):
        self.roll(range(5))
        return self.dice

    def value(self):
        return self.dice[:]
    def getScore(self):
        return self.score

    def score(self):
        counts = [0]*7
        for x in self.dice:
            counts[x] = counts[x] + 1
        if 6 in counts:
            return "six of a kind ",3000
        elif 5 in counts:
            return "five of a kind", 2000
        elif 4 in counts:
            return "four of a kind", 1000
        elif 3 in counts:
            x = 100 * counts.index(3)
            return "three of a kind", x
        elif not 2 in counts:
            return "Straight ", 2000
        else:
            return "you roll Gabage", 0
        
