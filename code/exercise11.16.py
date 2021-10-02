class statSet:
    def __init__(self):
        self.statset = []
    def addNumber(self,x):
        self.statset.append(x)
        return self.statset
       
    def mean(self):
        self.sum = 0
        self.n = 0
        for x in self.statset:
            self.n += 1
            self.sum+=x
        return (self.sum/self.n)
    def median(self):
        n = 0
        for x in self.statset:
            n+=1
        if n%2==0:
            b = int(n/2)
            self.median = (self.statset[b] + self.statset[b-1])/2
            return   self.median
        else:
            b = (n-1)/2
            self.median = self.statset[b]
            return self.median
        
            
            
    def stdDev(self):
        self.stdDev = 0
        for x in self.statset:
            self.stdDev = self.stdDev + (x-self.mean())**2/(self.n-1)
        return self.stdDev

    def count(self):
        self.count = 0
        for x in self.statset:
            self.count += 1
        return self.count
    def min(self):
        self.min = self.statset[0]
        for x in self.statset:
            if x > self.min:
                continue
            else:
                self.min = x
        return self.min
            
    def max(self):
        self.max = self.statset[0]
        for x in self.statset:
            if x < self.max:
                continue
            else:
                self.max = x
        return self.max

def main():
    statistics = statSet()
    ans = statistics.addNumber(5)
    statistics.addNumber(5)
    statistics.addNumber(5)
    statistics.addNumber(5)
    statistics.addNumber(9)
    mean = statistics.mean()
    statistics.addNumber(4)
    median = statistics.median()
    print(ans)
    print(mean)
    print(median)
    a = statistics.count()
    print(statistics.stdDev())
    print(a)

main()
        
