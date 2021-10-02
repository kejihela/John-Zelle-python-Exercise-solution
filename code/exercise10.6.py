class student:
    def __init__(self, qpoint,credit):
        self.qpoint = float(qpoint)
        self.credit = float(credit)
        

    def getcredit(self):
        return self.credit
    
    def getqpoint(self):
        return self.qpoint
    
    def addgrade(self, gradepoint, credit):
        self.qpoint =self.qpoint + (gradepoint * credit)
        self.credit  = self.credit + credit

    def addLetter(self, letter, credit):
        self.qpoint =self.qpoint + (letter * credit)
        self.credit  = self.credit + credit
        
    
    def getGPA(self):
        return self.qpoint/self.credit

def main():
    n = int(input("How many course are you offering "))
    student1 = student(0,0)
    for i in range(n):
        result = input("input your details with a space ")
        x,y = result.split()
        if x=="a" or x=="A":
            x=5
        elif x=="b" or x=="B":
            x = 4
        elif x=="c" or x=="C":
            x= 3
        elif x=="d" or x=="d":
            x=0
        elif x=="e" or x=="E":
            x=0
        else:
            x=0
        student1.addLetter(int(x),int(y))
    print(student1.getGPA())
    print(student1.getqpoint())
    print(student1.getcredit())
   
       
if __name__ == '__main__':
    main()
        
    
    
        
