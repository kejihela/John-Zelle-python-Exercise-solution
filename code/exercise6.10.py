def acronym(word):
    acronym=[]
    word_split = word.split()
    for phrase in word_split:
        output= phrase[0].upper()
        acronym.append(output)
    output = "".join(acronym)
    return output
def main():
    print("print the acronym of the following phrase")
    word = input("please type in your phrase ")
    answer = acronym(word)
    print(answer)
    
main()
