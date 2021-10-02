from exercise12C4 import GuiInterface
from exercise12C1 import PokerApp
from exercise12c import Introduction
from exercise12C5 import Display

def main():
    intro = Introduction()
    play = intro.click()
    if play == "Let's Play":
        intro.close()
        show = Display()
        inter = GuiInterface()
        poker = PokerApp(inter)
        poker.run()
main()
