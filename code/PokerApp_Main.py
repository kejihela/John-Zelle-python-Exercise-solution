from textinterface import TextInterface
from pokerapp import PokerApp

def main():
    inter = TextInterface()
    poke = PokerApp(inter)
    poke.run()

main()
    
