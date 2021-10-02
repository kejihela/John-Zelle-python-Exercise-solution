class student:
    def __init__(self, name, hour, grade):
        self.name = name
        self.hour = float(hour)
        self.grade = float(grade)
    def get_name(self):
        return self.name

    def get_hour(self):
        return self.hour

    def get_grade(self):
        return self.grade
    def gpa(self):
        return self.grade/self.hour

def make_student(student_details):
    name, hour, grade = student_details.split("\t")
    return student( name,hour,grade)

def main():
    file_name= input("please, input the name of the file")
    infile = open(file_name, 'r')

    best = make_student(infile.readline())

    for line in infile:
        s = make_student(line)
        if s.gpa() > best.gpa():
            best = s

    infile.close()


    infile = open(file_name, 'r')
    
    best_list = []
    for line in infile:
        new = make_student(line)
        if best.gpa() == new.gpa():
            best_list.append(new)

    infile.close()
    for i in range(len(best_list)): 
        print("the name of the person is", best_list[i].get_name())
        print("the grade is ", best_list[i].get_grade())
        print("the number of hours is ", best_list[i].get_hour())
        print("the gpa is ", best_list[i].gpa())
        print('\n')

if __name__ == '__main__':
    main()
    
    
    
    
    
