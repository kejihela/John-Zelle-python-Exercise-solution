""" PYTHON FUNCTIONS """
def count(myList, x):
    n = 0
    for i in myList:
        if i == x:
            n += 1
    return n

def isin(myList, x):
    for i in myList:
        if i == x: 
            return True
        else:
            continue
    return False

def index(myList, x):
    n = 0
    for i in myList:
        n += 1
        if i == x:
            return n-1
def reverse(mylist):
    new_list = []
    n = 0
    k = 0
    for i in mylist:
        n+=1
        new_list.append(i)
    n = n-1
    for i in mylist:
        new_list[n-k] = i
        k+=1
    return new_list

def sort(mylist):
    new_list = []
    n = 0
    for i in mylist:
        for a in mylist:
            if i > a:
                if a in new_list:
                    continue
                else:
                    new_list.append(a)
    return new_list
    
            
    
        


def main():
    names = [1,2,2,2,4,4,4,4,6,7,3,4,3,2,4]
    answer1 = count(names, 4)
    print(answer1)

    answer2 = isin(names, 4)
    print(answer2)

    answer3 = index(names, 4)
    print(answer3)

    answer4 = reverse(names)
    print(answer4)

    answer4 = sort(names)
    print(answer4)
main()
