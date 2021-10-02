from tkinter.filedialog import askopenfilename, asksaveasfilename
def word_doc():
    print("This program is going to print the no of lines, words and chracter")
    file  = askopenfilename()
    script = open(file, "r")
    #document = script.readline()

    doc = 0
    output = 0
    acc = 0
    for line in script:
        doc = doc + 1
        word = line.split()
        for w in word:
            acc = acc + 1
            x = "".join(w)
            for character in x:
                output = output + 1
                print(character)
    
            
    print(doc,acc, output,)
word_doc()
        
    
