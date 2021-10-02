#def file():
    #print("This program will make us edit a file")
    #file_name = "script.txt"
   # file = open(file_name, "r")
    #data = file.read()
    #print(data)

def file_line():
    file_name = "script.txt"
    file = open(file_name, "r")
    for i in range(5):
        data = file.readlines()
        print(data[:-1])

file_line()
