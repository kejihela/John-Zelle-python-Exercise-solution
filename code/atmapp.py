from User import User
from transfer import Transfer
from graphics import *
from withdrawer import Withdraw
from ATMinterface import Interface
from accbalance import AccBalance
class ATMapp:
    def __init__(self,interface,transfer,AccBalance,withdraw):
        self.interface = interface
        self.transfer = transfer
        self.AccBalance = AccBalance
        self.withdraw = withdraw
        


    def run(self):
        self.user = self.read_file()
        self.person = self.login()
        if self.person == None:
            return None
        
        else:
            self.person = self.AccType()
            if self.person == None:
                return None
                
            else:
                label = self.operation()
                if label == None:
                    pass
        self.writefile(self.user)
        return None
 

    def read_file(self):
        list1 = []
        infile = open("customer.txt", "r")
        for line in infile.readlines():
            if line == "\n":
                continue
            else:
                a, b, c, d, e = line.split("\t")
                list1.append(User(a,b,c,d,e))
        infile.close()
        return list1
    
    def login(self):
        pin, Id = self.interface.login()
        if pin == None:
            return None
        else:
            for person in self.user:
                if pin == int(person.pin):
                    a = person
                    if Id == int(a.ID):
                        return a
                    else:
                        self.error()
                else:
                    continue
            
    
    def AccType(self):
        label = self.interface.accType()
        if label==self.person.getAccType():
            return self.person
        else:
            self.error()
        
    def operation(self):
        label = self.interface.operations()
        if label == "BALANCE":
            label = self.AccBalance.Balance(self.person.AccBalance)
            if label == "OK":
                self.success()
                label = self.logout()
                if label == "NO":
                    self.exit()
                else:
                    self.run()
                    
                
        
        elif label == "WITHDRAW":
            label = self.withdraw.cash()
            if self.person.AccBalance > int(label):
                self.person.AccBalance = self.person.AccBalance - float(label)
                self.success()
                label = self.logout()
                if label == "NO":
                    self.exit()
                else:
                    self.run()
            else:
                self.insufficient()
                label = self.logout()
                if label == "NO":
                    self.exit()
                else:
                    self.run()
                
            
        elif label == "TRANSFER":
            cash, label = self.transfer.cash()
            if self.person.AccBalance > cash:
                self.person.AccBalance = self.person.AccBalance - cash
                if label == "OK":
                    self.success()
                    label = self.logout()
                    if label == "NO":
                        self.exit()
                    else:
                        self.run()
                
            else:
                self.insufficient()
                label = self.logout()
                if label == "NO":
                    self.exit()
                else:
                    self.run()
                

    def error(self):
        label = self.interface.error()
        if label == "YES":
            self.run()
        elif label == "NO":
            self.exit()      
            
    def exit(self):
        self.interface.exit()

    def logout(self):
        self.interface.logout()

    def success(self):
        self.interface.success()
         
        
    def close(self):
        self.interface.close()

    
    def writefile(self, lst):
        infile = open("customer.txt", "w")
        write_string = ""
        n = 0
        for person in lst:
            n=0
            for personal in [person.getPin(),person.getID(),person.getAccBalance(),person.getAccType(),person.getName()]:
                if n == 4:
                    write_string += str(personal) + "\n"
                else:
                    
                    write_string += str(personal) + "\t"
                n+=1
        print("{0}".format(write_string), file = infile)
        infile.close()

    def insufficient(self):
        self.transfer.insufficient()
        
            
            
            

        

    
    
                 
        
                    

        
        
        
        
        
        
    
