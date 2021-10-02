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
        print(s,file=outfile)
    outfile.close()

def main():
    new_list = {}
    new_list1 = []
 
    filename = input("please input the name of the file ")
    data = readFile(filename)
    for s in data:
        new_list[s.get_name()] =  s.gpa(),s.get_name()
    item = list(new_list.values())
    item.sort()


    filename = input("please input the name of the file ")
    writeFile(item,filename)
    print("file has been printed")

if __name__ == '__main__':
              main()
    
        
