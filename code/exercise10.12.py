from random import randrange
from graphics import *
class poker:
    def __init__(self,win, rank, suit):
        self.win = win  
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
            
    def draw(self,win,center):
        poker_image = Image(center, "ace_of_heart.gif")
        poker_image.draw(win)
                   
     
def main():
    win = GraphWin("Poker Game", 1200, 500)
    win.setCoords(0,0,5,5)
    print("The poker Game")
    poker1 = poker(win, 2, "s")
    poker1.draw(win, Point(0.5,1.5))
    poker1.draw(win, Point(1.5,1.5))
    poker1.draw(win, Point(2.5,1.5))
    poker1.draw(win, Point(3.5,1.5))
    poker1.draw(win, Point(4.5,1.5))
if __name__ == '__main__':
    main()
        
