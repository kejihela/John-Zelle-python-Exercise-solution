from exercise12Bgui import GuiInterface
from pokerapp import PokerApp
from exercise12c import Introduction

def main():
    intro = Introduction()
    play = intro.click()
    if play == "Let's Play":
        intro.close()
        inter = GuiInterface()
        poker = PokerApp(inter)
        poker.run()
main()
