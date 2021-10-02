class Attendee:
    def __init__(self,name,company, state, mail):
        self.name = name
        self.company = company
        self.state = state
        self.mail = mail


    def getName(self):
        return self.name

    def getCompany(self):
        return self.company

    def getState(self):
        return self.state

    def getMail(self):
        return self.mail

    def __str__(self):
        return "name: "+ self.name + "\n" \
                "email: " + self.mail

    def getDetails(self):
        return self.name,self.company,self.state,self.mail
