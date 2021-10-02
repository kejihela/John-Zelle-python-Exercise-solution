from random import randrange
class Dice:
    def __init__(self):
        self.dice = [0]*5
        self.rollAll()
        
    def roll(self, inputs):
        for value in inputs:
            self.dice[value] = randrange(1,7)
        return self.dice

    def rollAll(self):
        self.roll(range(5))
        return self.dice

    def value(self):
        return self.dice[:]

    def score(self):
        counts = [0]*7
        for value in self.dice:
            counts[value] = counts[value] + 1

        if 5 in counts:
            return "5 of a kind", 30
        elif 4 in counts:
            return "4 0f a kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full house", 12
        elif 3 in counts:
            return "3 of a kind", 8
        elif not(2 in counts) and (counts[1]==0 or counts[6]==0):
            return "straight", 20
        elif counts.count(2)==2:
            return "Two pairs", 5
        else:
            return "Garbage", 0

    
            
        
