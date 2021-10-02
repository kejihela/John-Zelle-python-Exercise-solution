class TextInterface:
    def __init__(self):
        print("welcome to poker Game")

    def setMoney(self, amt):
        print("you have ${0} left".format(amt))

    def setDice(self, value):
        print("Dice: ", value)

    def wantToPlay(self):
        ans = input("Do you wan to continue the Game ")
        return ans[0] in "Yy"

    def close(self):
        print("\nThanks for Playing")

    def showResult(self, msg, score):
        print("{0} you win ${1} ".format(msg,score))
    def chooseDice(self):
        return eval(input("input the index you wish to change([] to Quit)"))
        
