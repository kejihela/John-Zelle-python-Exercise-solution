def pin(filename, filename1):
    list1= []
    list2 = []
    list3 = []
    list4 = []
    
    text = open(filename, "r").read()
    text = text.lower()
    for ch in '!"#$%&0*+,-./:;<=>?<0[\\]-_{1}-':
        text = text.replace(ch,' ')
    word = text.split()
    for line in word:
        list1.append(list(line))

    inline = open(filename1, "r").read()
    inline = inline.lower()
    for ch in '!"#$%&0*+,-./:;<=>?<0[\\]-_{1}-':
        text = text.replace(ch,' ')
    inline = inline.split()
    for things in inline:
        list2.append(list(things))

    for a in list1:
        for b in list2:
            if a==b:
                n=len(a)
                b="x"*n
                list3.append(b)
        else:
            list3.append(a)
    for x in list2:
        list3.remove(x)
    for i in list3:
        list4.append("".join(i))
    
            

    listToStr = ' '.join([str(elem) for elem in list4])

    return  listToStr, text, list2

def main():
    filename = input("Please, input the name of your file ")
    filename1 = input("Please, input the name of your file ")
    answer, solution, a = pin(filename,filename1 )
    print(answer, "\n",  solution, '\n', a)
main()

