def acronym():
    print("print the acronym of the following phrase")
    word = input("please type in your phrase ")
    word_split = word.split()
    acronym=[]
    for phrase in word_split:
        output= phrase[0].upper()
        acronym.append(output)
    output = "".join(acronym)
    print(output)

acronym()
