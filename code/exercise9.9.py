from random import randrange
def main():
    introduction()
    n = getInputs()
    simulate(n)
    
   
def introduction():
    print("This powerful program simulation program that runs multiple")
    print("hands of blackjack for each possible starting value (ace-10) and")
    print("estimates the probability that the dealer busts for each")
    print("starting value.")
def getInputs():
    while True:
        a = int(input("How many games did you want to simulate "))
        if a <= 0:
            print("please input number greater than zero")
        else:
            return a


def simulate(n):
    sum_burst = sum_win = 0
    blackjack = [2,3,4,5,6,7,8,9,10,10,10,11]
    for j in blackjack:
        good = bad =  0
        for i in range(n):
            score = j
            while not gameOver(score):
                jack = blackjack[randrange(len(blackjack))]
                if jack == 11 and (score >=7 and score <=11):
                    score = score + 10
                    good = good + 1
                elif jack == 11 and (score < 7 or score > 11):
                    score = score + 1
                    if score >=17 and score <=21:
                        good = good + 1
                    elif score >21:
                        bad = bad + 1
                    else:
                        continue
                else:
                    score = score + jack
                    if score >=17 and score <=21:
                        good = good + 1
                    elif score >21:
                        bad = bad + 1
                    else:
                        continue
        a = bad + good
        print("the probability for dealer busting in ", j , "is" ,bad/a)
        
   
            
            

            
def gameOver(score):
    return score >=17

    
                
            
        

if __name__ == '__main__' : main()


