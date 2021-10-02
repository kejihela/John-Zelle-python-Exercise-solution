def names():
    print("This program is about to print the username of some names")
    file_name = "name.txt"
    input_file = open(file_name, "r")
    output_file = open("username", "w")
    for line in input_file:
        last, first =line.split()
        uname = last[0] + first[:7]
        print(uname, file = output_file)
names()
