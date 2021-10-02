from attendee import Attendee
from interface import Interface
class AttendeeApp:
    def __init__(self,filename, interface):
        self.interface = interface
        self.filename = filename

    def choose(self):
        choice = self.interface.choose()
        [self.add, self.deletes,self.lst_info,self.lst_state,self.quits][choice-1]()
        if choice != 5:
            return True
        else:
            return False
        

    def add(self):
        a,b,c,d = self.interface.add()
        self.attendee.append(Attendee(a,b,c,d))

    def deletes(self):
        self.interface.deletes(self.attendee)

    def lst_info(self):
        self.interface.lst_info(self.attendee)

    def lst_state(self):
        self.interface.lst_state(self.attendee)


    def readfile(self):
        list1 = []
        infile = open(self.filename, "r")
        for line in infile.readlines():
            if line == "\n":
                continue
            else:
                a,b,c,d= line.split("\t")
                list1.append(Attendee(a,b,c,d))
        infile.close()
        return list1

    def writefile(self, lst):
        infile = open(self.filename, "w")
        write_string = ""
        n = 0
        for person in lst:
            n=0
            for personal in person:
                if n == 3:
                    write_string += personal + "\n"
                else:
                    
                    write_string += personal + "\t"
                n+=1
        print("{0}".format(write_string), file = infile)
        infile.close()

    def quits(self):
        self.interface.quits()
        
        

    def run(self):
        self.attendee = self.readfile()
        cons = True
        while cons:
            self.interface.Menu()
            cons = self.choose()
        self.writefile(self.attendee)
   
