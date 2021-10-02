def change():
    print("This program is about to print your change")
    quarter = int(input("enter your value: "))
    Dime = int(input("enter your value: "))
    pennies = int(input("enter your value: "))
    nickel = int(input("enter your value: "))

    total = (quarter * 25 + Dime * 10 + pennies*1 * nickel * 5)
    print("the total is ${0}.{1:0>2}".format(total//100,total%100))
change()
    
