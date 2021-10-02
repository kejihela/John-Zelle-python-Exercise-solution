def trait_robust():
    print("The value of the inputed name is printed in this program")
    name = input("Please input your name ").split()
    message = "".join(name)
    output = 0
    for i in message:
        output = ord(i) + output - 96
    print(output)
trait_robust()
