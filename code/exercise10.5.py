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
    
    def getGPA(self):
        return self.qpoint/self.credit

def main():
    n = int(input("How many course are you offering "))
    student1 = student(0,0)
    for i in range(n):
        result = input("input your details with a space ")
        x,y = result.split()
        student1.addgrade(int(x),int(y))
    print(student1.getGPA())
    print(student1.getqpoint())
    print(student1.getcredit())
   
       
if __name__ == '__main__':
    main()
        
    
    
        
