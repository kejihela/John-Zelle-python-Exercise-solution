from random import random
def main():
    introduction()
    n, probA, probB = getInput()
    winA, winB, shootoutA,shootoutB  = sumNgames(n , probA, probB)
    Result(winA, winB, shootoutA, shootoutB)


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
    winA = winB = shootoutA = shootoutB = 0
    for i in range(n):
        scoreA, scoreB = simNUMgames(probA, probB, i)
        if scoreA > scoreB:
            winA = winA + 1
            if scoreA ==11 and scoreB ==0:
                shootoutA = shootoutA + 1
            else:
                continue
                
        else:
            winB = winB + 1
            if scoreB ==11 and scoreA ==0:
                shootoutB = shootoutB + 1
            else:
                continue
    return winA, winB, shootoutA, shootoutB

def simNUMgames(probA, probB, i):
    if i%2 != 0:
        serving = "A"
    else:
        serving = "B"
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
     return a == 15 or b == 15 or (a==11 and b==0)or (a==0 and b==11)
def Result(winA, winB, shootoutA, shootoutB):
    n = winA + winB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winA, winA/n))
    print("Wins for B: {0} ({1: 0.1%})".format(winB, winB/n))
    print("shootout for A: {0} ({1: 0.1%})".format(shootoutA, shootoutA/n))
    print("shootout for B: {0} ({1: 0.1%})".format(shootoutB, shootoutB/n))

if __name__ == '__main__' : main()





            
    
    
