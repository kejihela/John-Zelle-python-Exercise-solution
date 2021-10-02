import random

def shuffle(mylist):
    list2 = []
    list3 = []
    n = 0
    for i in mylist:
        n+=1
    for i in mylist:
        value = random.sample(mylist, n)
    list2.append(value)
    for i in list2:
        for a in i:
            list3.append(a)
    return list3
        
def main():
    names = [1,2,2,2,4,4,4,4,6,7,3,4,3,2,4]
    answer = shuffle(names)
    print(answer)

main()
