from random import randrange
class poker:
    def __init__(self, rank, suit):
        self.rank = int(rank) 
        self.suit = str(suit) 
        self.value = 0
        self.value1 = 0

    def getRank(self):
        return self.rank

    def getSuit(self):
        if self.suit == "d":
            return  "diamond"
        elif self.suit == "c":
            return "clubs"
        elif self.suit == "h":
            return "heart"
        elif self.suit == "s":
            return  "spades"
        else:
            return "no suit"

    def getValue(self):
        if 11 <= self.rank <= 13:
            return  10
        else:
            return self.rank

    def __str__(self):
        if self.getRank() == 1:
            if self.getSuit() == "diamond":
                return "Ace  Diamond"
            elif self.getSuit() == "clubs":
                return "Ace  clubs"
            elif self.getSuit() == "heart":
                return "Ace  heart"
            else:
                return "Ace  spade"
        elif self.getRank() == 11:
            if self.getSuit() == "diamond":
                return "jack  Diamond"
            elif self.getSuit() == "clubs":
                return "jack  clubs"
            elif self.getSuit() == "heart":
                return "jack  heart"
            else:
                return "jack  spade"
        elif self.getRank() == 12:
            if self.getSuit() == "diamond":
                return "queen  Diamond"
            elif self.getSuit() == "clubs":
                return "queen  clubs"
            elif self.getSuit() == "heart":
                return "queen  heart"
            else:
                return "queen of spade"
        elif self.getRank() == 13:
            if self.getSuit() == "diamond":
                return "king Diamond"
            elif self.getSuit() == "clubs":
                return "king clubs"
            elif self.getSuit() == "heart":
                return "king  heart"
            else:
                return "king  spade"
        else:
            if self.getSuit() == "diamond":
                return str(self.getRank()) + "  Diamond"
            elif self.getSuit() == "clubs":
                return str(self.getRank()) + " clubs"
            elif self.getSuit() == "heart":
                return str(self.getRank()) + "  heart"
            else:
                return str(self.getRank()) + "  spade"
def output(filename,a):
    pass
    
    

def main():
    print("The poker Game")
    filename = input("please, enter the name of your file")
    n = int(input("please, input the number of cards youintend to draw "))
    word = []
    blackjack = 0
    for i in range(n):
        value = randrange(1, 14)
        value1 = randrange(1, 5)
        if value1 == 1:
            value1 = "d"
        elif value1 == 2:
            value1 = "c"
        elif value1 == 3:
            value1 = "h"
        else:
            value1 = "s"
        poker1 = poker(value, value1)
        #output(filename, poker1)
        word.append(str(poker1))
        result = poker1.getValue()
        print(poker1)
        blackjack = blackjack + result
    
    text = open(filename, "w")
    print(word, file=text)
    text.close
    print("DONE!!!")
    for i in word:
        
    
    
    print("blackjack: ",blackjack  )
    
if __name__ == '__main__':
    main()
        
