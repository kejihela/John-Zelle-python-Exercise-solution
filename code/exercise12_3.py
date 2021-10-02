from attendee import Attendee
class AttendeeApp:
    def __init__(self,filename):
        #self.interface = interface
        self.filename = filename
        

    
    def addAttendee(self):

        self.lst = []
        a,b,c,d,e = self.getInput()
        self.lst.append(Attendee(a,b,c,d))

    def getInput(self):
        n=input("input id number")
        name = input("input id name")
        company = input("input id company")
        state = input("input id state")
        mail = input("input id mail")
        return n,name,company,state,mail

                 
    def display(self):
        for x in self.list1:
            print(x)

    def readFile(self):
        list1 = []
        infile = open(self.filename, "r")
        for line in infile.readlines():
            if line == "\n":
                continue
            else:
                a,b,c,d= line.split("\t")
                list1.append(Attendee(a,b,c,d))
        return list1
    def writeFile(self, lst):
        infile = open(self.filename, "w")
        write_string = ""
        #for func in 
        
            
def main():
    filename = "ok.txt"
    files = AttendeeApp(filename )
    show = files.readFile()
    print(show)
    
    
    
    


main()
