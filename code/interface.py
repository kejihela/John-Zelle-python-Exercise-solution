class Interface:
    def Menu(self):
        print("---------MENU---------")
        print("1. Add  ")
        print("2. Delete ")
        print("3. Details ")
        print("4. Search by state ")
        print("5. Quit ")

    def choose(self):
        choice = eval(input("please inputs between 1-5 "))
        return choice
              
    def add(self):
        a = input("please input you name ")
        b = input("please input you company ")
        c = input("please input you state ")
        d = input("please input you mail ")
        return a,b,c,d

    def deletes(self, lst):
        name = input("please, input the name to delete ")
        for person in lst:
            if person.getName() == name:
                del lst[lst.index(person)]

    def lst_info(self, lst):
        for person in lst:
            print(person.getName(), person.getMail())

    def lst_state(self, lst):
        state = input("please, input the state ")
        for person in lst:
            if person.getState() == state:
                print(person.getName(), person.getMail())

    def quits(self):
        return False
        
        
