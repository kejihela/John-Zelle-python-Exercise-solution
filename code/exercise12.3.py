class Attendee:
    def __init__(self, filename):
        self.filename = filename
        self.process(self.filename)
        

                    
                       
                
    def display(self):
        return self.attendee 
            
    def process(self,filename):
        self.attendee  = []
        infile = open(filename, "r")
        for line in infile.readlines():
            if line == "\n":
                continue
            else:
                self.name, self.company,self.state, self.email= line.split("\t")
                self.attendee.append([self.name, self.company,self.state, self.email])

        
    def name_email(self):
        for x in self.attendee:
            print(self.attendee)
                
            






    def addAttendee(self):
        list2 = []
        a,b,c,d,e = self.getInput()
        for i in (a,b,c,d,e):
            list2.append(i)
        self.list1.append(list2)
        outfile = open(self.filename, "w")
        for line in self.list1:
            for i in line:
                print("{0}".format(i), file=outfile)
        #self.process()
        print(self.list1)
            

    def delAttendee(self):
        pass

    def getInput(self):
        n=input("input id number")
        name = input("input id name")
        company = input("input id company")
        state = input("input id state")
        mail = input("input id mail")
        return n,name,company,state,mail
        
def main():
    #filename = input("Please, input your file name ")
    files = Attendee("ok.txt")
   
    #files.addAttendee()
    show = files.name_email()
    print(show)
    #n,name,company,state,mail = files.getInput()
    #print( n,name,company,state,mail)


main()
