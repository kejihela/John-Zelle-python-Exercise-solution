from random import random
def simOnegame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        if serving == "B":
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB
def gameOver(a, b):
    return a == 15 or b == 15

scoreA, scoreB = simOnegame(0.7,0.9)
print(scoreA, scoreB)
