from tkinter.filedialog import askopenfilename, asksaveasfilename
def batch():
    print("This program will print a chaotic computation using file")
    n = eval(input("please input the number of iterations "))
    file_name1 = askopenfilename()
    file_name2 = askopenfilename()
    #output_file = asksaveasfilename()
    x_value = open(file_name1, "r")
    x= float(x_value.read())
    y_value = open(file_name2, "r")
    y = float(y_value.read())

    for i in range(n):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print("the outputs are ,", x,"..",y)
batch()
    
    
    
