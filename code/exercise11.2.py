from student import Student,make_student
def readFile(filename):
    infile = open(filename, 'r')
    student = []
    for line in infile:
        student.append(make_student(line))

    infile.close()
    return student

def writeFile(student, filename):
    outfile = open(filename, 'w')
    for s in student:
        print("{0}\t{1}\t{2}".format(s.get_name(), s.get_hour(), s.gpa()),file=outfile)
    outfile.close()

def main():
    infile = input("please, enter the name of your input file ")
    outfile = input("please, enter the name of your output file ")
    sort = input("please, input the type of sort you waned to perform ")
    data = readFile(infile)
    if sort == "gpa":
        data.sort(key=Student.gpa)
    elif sort == "name":
        data.sort(key=Student.get_name)
    elif sort == "hour":
        data.sort(key=Student.get_hour)
    writeFile(data, outfile)
    print("DONE!!!")
    
        
    
if __name__ == '__main__':
    main()
    
        
