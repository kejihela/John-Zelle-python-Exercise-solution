from random import randrange 
def main():
    Introduction()
    n = getInputs()
    burst, win = simBlackjack(n)
    Result(burst, win) 
def Introduction():
    print("This program is about to estimate the probability")
    print("that a dealer will burst")
    print("stay tune")
def getInputs():
    while True:
        a = int(input("How many games did you want to simulate "))
        if a <= 0:
            print("please enter number between 1 to infinity")
        else:
            return a
def simBlackjack(b):
    burst = 0
    win = 0
    for i in range(b):
        good, bad = simNgames()
        burst = burst + bad
        win = win + good
    return burst, win

def simNgames():
    score = 0
    good = 0
    bad = 0
    blacklist = [2,3,4,5,6,7,8,9,10,10,10,11]
    while not gameOver(score):
        jack = blacklist[randrange(len(blacklist))]
        if jack == 11 and (score >= 7 and score <=11):
            score = score + 10
            good = good + 1
        elif jack == 11 and (score < 6 or score > 10):
            score = score + 1
            if score >=17 and score <=21:
                good = good + 1
            elif score < 17:
                continue
            else:
                bad = bad + 1
        else:
            score = score + jack
            if score >=17 and score <=21:
                good = good + 1
            elif score < 17:
                continue
            else:
                bad = bad + 1
       
    return good, bad       
    
    
def gameOver(score):
    return score >=17

def Result(burst, win):
    n = burst + win
    print("The total number of simulated game is ", n)
    print("The probability of dealer bursting is ", burst/n)
    print("The probability of dealer winning is ", win/n)
    print("I pray this makes sense")

if __name__=='__main__' : main()









    
