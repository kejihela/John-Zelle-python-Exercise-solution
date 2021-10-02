from tkinter.filedialog import askopenfilename
def squareEach(square_n):
    acc= []
    for i in square_n:
        i = int(i)
        square = i**2
        acc.append(square)
    return acc
def sumEach(sum_n):
    acc= 0
    for i in sum_n:
        i = int(i)
        acc = acc + i
    return acc
def main():
    print("This program print the value of the sum of square of numbers")
    name = askopenfilename()
    file_name = open(name, "r")
    values = file_name.readlines()
    the_square = squareEach(values)
    print(the_square)
    the_sum = sumEach(the_square)
    print(the_sum)
main() 
    
