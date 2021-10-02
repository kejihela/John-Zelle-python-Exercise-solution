from random import random
def main():
    introduction()
    n, probA, probB = getInput()
    winA, winB = sumNgames(n , probA, probB)
    Result(winA, winB)


def introduction():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")
def getInput():
    a = float(input("Please input the probability for player A "))
    b = float(input("Please input the probability for player B "))
    n = int(input("Please input the number of games played "))
    return n, a, b
def sumNgames(n, probA, probB):
    winA = winB = 0
    for i in range(n):
        scoreA, scoreB = simNUMgames(probA, probB)
        if scoreA > scoreB:
            winA = winA + 1

        else:
            winB = winB + 1
    return winA, winB

def simNUMgames(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB
def gameOver(a, b):
     return a == 15 or b == 15
def Result(winA, winB):
    n = winA + winB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winA, winA/n))
    print("Wins for B: {0} ({1: 0.1%})".format(winB, winB/n))

if __name__ == '__main__' : main()

gameOver(0,0)



            
    
    
