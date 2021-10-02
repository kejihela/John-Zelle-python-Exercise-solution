from random import randrange
def main():
    introduction()
    n = getInputs()
    win,lose = simulation(n)
    conclusion(win, lose)
    
    
def introduction():
    print("This program will print the probability of a player winning")
    print("A crap game")
def getInputs():
    a = int(input("How many games did you want to play "))
    return a

def simulation(n):
    win = lose = 0
    for i in range(n):
        dice = roll_dice()
        good, bad = casino(dice)
        win = win + good
        lose = lose + bad
    return win, lose

def roll_dice():
    dice_1 = randrange(1,7)
    dice_2 = randrange(1,7)
    b = dice_1 + dice_2
    return b
   
def casino(dice):
    bad = 0
    good = 0
    if dice == 2 or dice == 3 or dice == 12:
        bad = bad + 1
    elif dice == 7 or dice == 11:
        good = good + 1
    else:
        dices = roll_dice()
        while dices != 7 and dices != dice:
            dices = roll_dice()
        if dices == 7:
            bad = bad + 1
        else:
            good = good + 1
    return good, bad
def conclusion(win, lose):
    n = win + lose
    print("\n the total number of games simulated is: ", n)
    print("The number of wins is ", win)
    print("The number of lose is ", lose)
    print("the probabiity of winning a game is ", win/n)
    
if __name__ == '__main__' : main()    
        
    
