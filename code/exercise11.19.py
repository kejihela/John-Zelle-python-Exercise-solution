class classical_set():
    def __init__(self, element):
        self.element = element
    def set(self):
        return self.element
    def addElement(self,x):
        self.element.append(x)
    def deleteElement(self, x):
        for a in self.element:
            if x == a:
                self.element.remove(x)
            else:
                continue
        print(x, "successfully deleted")
    
    def member(self, x):
        if x in self.element:
            return True
        else:
            return False
    def intersection(self, set2):
        for x in set2:
            if x in self.element:
                continue
            else:
                self.element.append(x)
        return self.element
    
    def union(self, set2):
        list1 = []
        for x in self.element:
            for b in set2:
                if x == b:
                    list1.append(x)
        return list1
    def subtract(self, set2 ):
        list1 = []
        for x in set2:
            for b in self.element:
                if x == b:
                    continue
                else:
                    list1.append(x)
        return list1
def main():
    set1 = classical_set([3,5,7,9,2])
    print(set1.intersection([1,4,5,8,9,6]))
    #print(set1.set())
main()

        
    
        
        
