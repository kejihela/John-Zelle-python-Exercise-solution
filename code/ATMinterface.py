from button import Button
from graphics import *
import time
class Interface:
    def __init__(self, win):
        self.win = win
        self.banner = Text(Point(3,3.5), "WELCOME TO KEJI'S BANK")
        self.banner.setStyle("bold")
        self.banner.setFill("black")
        self.banner.setSize(12)
        self.banner.draw(self.win)

    def login(self):
        self.banner.setText("LOGIN YOUR ACCOUNT")
        pin_text = Text(Point(2,2.5), "PIN").draw(self.win)
        ID_text = Text(Point(2,1.5), "ID").draw(self.win)
        pin = Entry(Point(3,2.5),10)
        pin.setText("PIN")
        pin.draw(self.win)
        ID = Entry(Point(3,1.5),10)
        ID.setText("ID")
        ID.draw(self.win)
        bttn1 = Button(self.win,Point(1,1),0.8,0.6,"LOGIN")
        bttn1.activate()
        bttn2 = Button(self.win,Point(5,1),0.8,0.6,"CANCEL")
        bttn2.activate()
        pt = self.win.getMouse()
        a = int(pin.getText())
        b = int(ID.getText())
        if bttn1.clicked(pt):
            pin_text.undraw()
            ID_text.undraw()
            pin.undraw()
            ID.undraw()
            bttn1.undraw()
            bttn2.undraw()
            return a,b
        elif bttn2.clicked:
            pin_text.undraw()
            ID_text.undraw()
            pin.undraw()
            ID.undraw()
            bttn1.undraw()
            bttn2.undraw()
            return self.exit(),1
            
        
        
        
        
    def accType(self):
        self.banner.setText("ENTER YOUR ACCOUNT TYPE")
        bttn1 = Button(self.win,Point(0,1.5),0.9,0.6,"SAVINGS")
        bttn1.activate()
        bttn2 = Button(self.win,Point(0,2.5),0.9,0.6,"CURRENT")
        bttn2.activate()
        pt = self.win.getMouse()
        cons = True
        while cons:
            if bttn1.clicked(pt):
                cons = False
                bttn1.undraw()
                bttn2.undraw()
                return bttn1.getLabel()
            
            elif bttn2.clicked(pt):
                cons = False
                bttn1.undraw()
                bttn2.undraw()
                return bttn2.getLabel()
           

    def operations(self):
         self.banner.setText("WHAT OPERATION DO YOU WANT TO PERFORM")
         bttn1 = Button(self.win,Point(0,2.5),1,0.6,"BALANCE")
         bttn1.activate()
         bttn2 = Button(self.win,Point(0,1.5),1,0.6,"WITHDRAW")
         bttn2.activate()
         bttn3 = Button(self.win,Point(0,0.5),1,0.6,"TRANSFER")
         bttn3.activate()
         pt = self.win.getMouse()
         if bttn1.clicked(pt):
             self.banner.setText("")
             bttn1.undraw()
             bttn2.undraw()
             bttn3.undraw()
             return bttn1.getLabel()
        
         elif bttn2.clicked(pt):
             self.banner.setText("")
             bttn1.undraw()
             bttn2.undraw()
             bttn3.undraw()
             return bttn2.getLabel()
         elif bttn3.clicked(pt):
             self.banner.setText("")
             bttn1.undraw()
             bttn2.undraw()
             bttn3.undraw()
             return bttn3.getLabel()
        
             

    def logout(self):
        self.banner.setText("DO YOU WANT TO PERFORM ANOTHER TRANSACTION")
        bttn1 = Button(self.win,Point(1,1),0.5,0.5,"YES")
        bttn1.activate()
        bttn2 = Button(self.win,Point(5,1),0.5,0.5,"NO")
        bttn2.activate()
        pt = self.win.getMouse()
        if bttn1.clicked(pt):
            bttn1.undraw()
            bttn2.undraw()
            return bttn1.getLabel()
                    
        elif bttn2.clicked:
            bttn1.undraw()
            bttn2.undraw()
            return bttn2.getLabel() 
                    

    def error(self):
        self.banner.setText("WRONG ACCOUNT INFORMATION, DO YOU WANT TO TRY AGAIN ")
        bttn1 = Button(self.win,Point(1,1),0.5,0.5,"YES")
        bttn1.activate()
        bttn2 = Button(self.win,Point(5,1),0.5,0.5,"NO")
        bttn2.activate()
        pt = self.win.getMouse()
        cons = True
        while cons:
            if bttn1.clicked(pt):
                cons = False
                bttn1.undraw()
                bttn2.undraw()
                return bttn1.getLabel() 
                    
            elif bttn2.clicked:
                cons = False
                bttn1.undraw()
                bttn2.undraw()
                return bttn2.getLabel()
                    
    def exit(self):
        self.banner.setText("THANK YOU FOR BANKING WITH US ")
        self.win.getMouse()
        return None
    
    
        

    def close(self):
        return self.win.close()

    def success(self):
        self.banner.setText("YOUR TRANSACTION IS COMPLETED ")
        self.win.getMouse()
        


    
        
        
    
        
        
        
        
        
            
             
        
            
        
        
        
    
        
        
        
        
        
        
        
        
