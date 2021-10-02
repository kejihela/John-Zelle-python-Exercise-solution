from tkinter.filedialog import askopenfilename, asksaveasfilename
def main():
    print("This programe will provide an output username")
    file_name = askopenfilename()
    output_file = asksaveasfilename()
    result = open(file_name, "r")
    result2 = open(output_file, "w")
    for line in result:
        first, last = line.split()
        uname = first[0:3] + last[:7]
        print(uname,file = result2)
main()
    
