from random import random
def main():
    introduction()
    n, probA, probB = getInputs()
    winA, winB = simNgames(n, probA, probB)
    result(winA, winB)

def introduction():
    print("This program will simulate the Table tennis game")
def getInputs():
    a = float(input("please enter the first player probability: "))
    b = float(input("please enter the second player probability: "))
    c = int(input("please input the number of games you want to simulate: "))
    return c, a, b
def simNgames(n, probA, probB):
    winA = winB = 0
    for i in range(n):
        scoreA, scoreB = simNUMgames(probA, probB)
        if scoreA > scoreB:
            winA = winA + 1
        else:
            winB = winB + 1
    return winA, winB
    
def simNUMgames(probA, probB):
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        serve = scoreA + scoreB 
        if serve <= 5 or (serve >=11 and serve <15):
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
    return scoreA, scoreB
            
def gameOver(scoreA, scoreB):
    return scoreA ==21 or scoreB==21

def result(winA, winB):
    n = winA + winB
    print("\n the total number of game simulated is: ", n)
    print("number of time A won is: {0}, ({1:0.1%})".format(winA, winA/n))
    print("number of time B won is: {0}, ({1:0.1%})".format(winB, winB/n))

if __name__ == '__main__' : main()


            
            
            
        
    
            
