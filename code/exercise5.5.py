def trait():
    print("The value of the inputed name is printed in this program")
    name = input("Please input your name ")
    output = 0
    for i in name:
        output = ord(i) + output - 96
    print(output)
trait()
              
