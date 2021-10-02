from random import random
def main():
    introduction()
    n, probA, probB = getInput()
    winA1, winB1 = sumNgames(n, probA, probB)
    winA2, winB2 = sumNgames(n, probA, probB)
    n1,n2,winA1,winA2 = Result(winA1, winB1, winA2, winB2)
    conclusion(n1,n2,winA1,winA2)
    
def introduction():
    print("This program simulates a game of Volleyball between two")
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
    winA1 = winB1 = 0
    for i in range(n):
        scoreA, scoreB = simNUMgames1(probA, probB)
        if scoreA > scoreB:
            winA1 = winA1 + 1

        else:
            winB1 = winB1 + 1
    return winA1, winB1

def sumNgames(n, probA, probB):
    winA = winB = 0
    for i in range(n):
        scoreA, scoreB = simNUMgames2(probA, probB)
        if scoreA > scoreB:
            winA = winA + 1

        else:
            winB = winB + 1
    return winA, winB

def simNUMgames1(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver1(scoreA, scoreB):
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
def gameOver1(a, b):
     return (a >= 15 or b >= 15) and abs(a - b) >= 2
    
def simNUMgames2(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver2(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            elif random()< probB:
                scoreB = scoreB + 1
                serving = "B"
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
        
            elif random()< probA:
                scoreA = scoreA + 1
                serving = "A"
            else:
                serving = "A"
    return scoreA, scoreB
def gameOver2(a, b):
     return (a == 25 or b == 25)

def Result(winA1, winB1, winA2, winB2):
    n1 = winA1 + winB1
    n2 = winA2 + winB2
    print("\nGames simulated for normal volleyball: ", n1)
    print("\nGames simulated for rally scoring volleyball: ", n2)
    print("Regular Wins for A in normal name: {0} ({1: 0.1%})".format(winA1, winA1/n1))
    print("Regular Wins for B in normal name: {0} ({1: 0.1%})".format(winB1, winB1/n1))
    print("Regular Wins for A in rally game: {0} ({1: 0.1%})".format(winA2, winA2/n2))
    print("Regular Wins for B in rally game: {0} ({1: 0.1%})".format(winB2, winB2/n2))
    return n1,n2,winA1,winA2

def conclusion(n1,n2,winA1,winA2):
    a = winA1/n1
    b = winA2/n2
    if abs(a - b) <= 2:
        print("Has no effect on relative advantage")
    elif abs(a - b) > 2:
        print("It magnifies the relative advantage")
    else:
         print("it reduces the advantage")
    

if __name__ == '__main__' : main()








            
    
    
