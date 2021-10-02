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
                return "Ace of Diamond"
            elif self.getSuit() == "clubs":
                return "Ace of clubs"
            elif self.getSuit() == "heart":
                return "Ace of heart"
            else:
                return "Ace of spade"
        elif self.getRank() == 11:
            if self.getSuit() == "diamond":
                return "jack of Diamond"
            elif self.getSuit() == "clubs":
                return "jack of clubs"
            elif self.getSuit() == "heart":
                return "jack of heart"
            else:
                return "jack of spade"
        elif self.getRank() == 12:
            if self.getSuit() == "diamond":
                return "queen of Diamond"
            elif self.getSuit() == "clubs":
                return "queen of clubs"
            elif self.getSuit() == "heart":
                return "queen of heart"
            else:
                return "queen of spade"
        elif self.getRank() == 13:
            if self.getSuit() == "diamond":
                return "king of Diamond"
            elif self.getSuit() == "clubs":
                return "king of clubs"
            elif self.getSuit() == "heart":
                return "king of heart"
            else:
                return "king of spade"
        else:
            if self.getSuit() == "diamond":
                return str(self.getRank()) + " of Diamond"
            elif self.getSuit() == "clubs":
                return str(self.getRank()) + " of clubs"
            elif self.getSuit() == "heart":
                return str(self.getRank()) + " of heart"
            else:
                return str(self.getRank()) + " of spade"

def main():
    print("The poker Game")
    n = int(input("please, input the number of cards youintend to draw "))
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
        print(poker1)
        result = poker1.getValue()
        print("The number ",i+1," card is ",result)
        blackjack = blackjack + result 
    print("blackjack: ",blackjack  )
    print(poker1)
if __name__ == '__main__':
    main()
        
