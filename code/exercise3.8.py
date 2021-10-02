def easter():
    print("This program will output the easter day")
    year = int(input("Please type in a year of 4 digits number "))
    C = year//100
    epact = (8+(C//4)-C +((8*C+13)//25 + 11*(year%19)))%30
    print("The day of easter is ", epact)
easter()

