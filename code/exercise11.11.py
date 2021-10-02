def pin(filename):
    list1= []
    list2 = []
    list3 = []
    
    text = open(filename, "r").read()
    text = text.lower()
    for ch in '!"#$%&0*+,-./:;<=>?<0[\\]-_{1}-':
        text = text.replace(ch,' ')
    word = text.split()
    for line in word:
        list1.append(list(line))
    for i in list1:
        if len(i) == 4:
            i = "xxxx"
            list2.append(i)
        else:
            list2.append(i)

    for i in list2:
        list3.append("".join(i))
    
    
    listToStr = ' '.join([str(elem) for elem in list3])
  
    print(listToStr)
    print (text)

def main():
    filename = input("Please, input the name of your file ")
    answer = pin(filename)
    #print(answer)
main()

