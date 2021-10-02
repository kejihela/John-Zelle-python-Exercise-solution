from tkinter.filedialog import askopenfilename, asksaveasfilename
def main():
    print("This program will compute the fuel efficiency of multi leg journey")
    odometer = eval(input("please input the start of the odometer "))
    infileName = askopenfilename()
    infile = open(infileName,"r" )
    car = []
    total = 0
   
    
    for line in infile:
        odo,gas = line.split(",")
        mpg = (int(odo) - odometer)/int(gas)
        car.append(mpg)
    print(car)
                    
    for j in car:
        total = total + j
    print("total", total)
main()
    
                          
    
                    
