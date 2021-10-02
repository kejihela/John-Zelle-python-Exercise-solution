from tkinter.filedialog import askopenfilename
def main():
    print("This program is about to print the coolness and hotness")
    hdd=0
    cdd=0
    infileName = askopenfilename()
    infile = open(infileName,"r" )
    for temp in infile:
        if int(temp) < 60:
            hdd = hdd + (60 - int(temp))
        elif int(temp) > 80:
            cdd = cdd + (int(temp) - 80)
        
    print("hot degree days",hdd, "cold degree days",cdd)
main()
        
            
