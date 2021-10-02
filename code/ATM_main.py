from User import User
from transfer import Transfer
from graphics import *
from withdrawer import Withdraw
from ATMinterface import Interface
from atmapp import ATMapp
from accbalance import AccBalance

def main():
    win = GraphWin("KEJI-BANK", 600,400)
    win.setCoords(-1,-1,6, 4)
    win.setBackground("green3")
    accBalance = AccBalance(win)
    inter = Interface(win)
    transfer = Transfer(win)
    withdraw = Withdraw(win)
    ATM = ATMapp(inter,transfer,accBalance,withdraw)
    answer = ATM.run()
    if answer == None:
        win.close()
    else: 
        ATM.run()


main()
    
    
