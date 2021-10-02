class User:
    def __init__(self,pin,ID,AccBalance,AccType,name):
        self.pin = pin
        self.ID = ID
        self.AccBalance = float(AccBalance)
        self.AccType = AccType
        self.name = name

    def getPin(self):
        return self.pin
    def getName(self):
        return self.name
    def getID(self):
        return self.ID

    def getAccBalance(self):
        return self.AccBalance

    def getAccType(self):
        return self.AccType

    def __str__(self):
        return "pin: " + self.pin + " ID: " + self.ID + "\n" \
               "AccountBal: " + str(self.AccBalance) + " AccType: "+ "\n" \
             + self.AccType + " name: " +self.name
               

    
        
