from exercise12Bgui import GuiInterface
from pokerapp import PokerApp

def main():
    inter = GuiInterface()
    poker = PokerApp(inter)
    poker.run()
main()
