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
        print("{0}\t{1}\t{1}".format(s.get_name(), s.get_hour(), s.get_grade()),file=outfile)
    outfile.close()

def main():
    filename = input("please input the name of the file ")
    data = readFile(filename)
    data.sort(key=Student.gpa)
    filename = input("please input the name of the file ")
    writeFile(data,filename)
    print("file has been printed")

if __name__ == '__main__':
    main()
    
        
