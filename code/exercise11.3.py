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
    sort_method = input("Sort in Ascending or Descending order, press A OR D? ")
    data = readFile(infile)
    if sort == "gpa":
        if sort_method == "A":
            data.sort(key=Student.gpa, reverse=True)
        else:
            data.sort(key=Student.gpa)
            
    elif sort == "name":
        if sort_method == "A":
            data.sort(key=Student.get_name,reverse=True)
        else:
            data.sort(key=Student.get_name)
            
    elif sort == "hour":
        if sort_method == "A":
            data.sort(key=Student.get_hour,reverse=True)
        else:
            data.sort(key=Student.get_hour)
            
    writeFile(data, outfile)
    print("DONE!!!")
    
        
    
if __name__ == '__main__':
    main()
    
        
