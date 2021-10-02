from random import random

def main():
    introduction()
    probA, probB, n = getInputs()
    winA, winB = simNgames(probA, probB, n)
    printSummary(winA, winB)
    
def introduction():
     print("This program prints the simulation of racqetball")
            

def getInputs():
    a = float(input("please, input the probability for player A "))
    b = float(input("please, input the probability for player B "))
    c = int(input("please how many games did you want to simulate "))
    return a, b, c

def simNgames(probA, probB, n):
    winA = 0
    winB = 0
    for i in range(n):
        scoreA, scoreB = simOnegame(probA, probB)
        if scoreA > scoreB:
            winA = winA + 1
        else:
            winB = winB + 1
    return winA , winB
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

def printSummary(winA, winB):
    n = winA + winB
    print("\n game simulated is ", n)
    print("wins for A is: {0}, ({1:0.1%})". format(winA, winA/n))
    print("wins for B is: {0}, ({1:0.1%})". format(winB, winB/n))
if __name__ =='__main__': main()
    
    
    
