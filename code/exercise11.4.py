from student import Student,make_student
from button import Button
from graphics import *

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
    
def getInput(win):
    Text(Point(1,4),"Input File").draw(win)
    Text(Point(1,3.5),"Output File").draw(win)
    infile = Entry(Point(2,4), 10).draw(win)
    outfile = Entry(Point(2,3.5), 10).draw(win)
    infile.setText("input_file")
    outfile.setText("Output_file")
    pt = win.getMouse()
    in_file = infile.getText()
    out_file = outfile.getText()
    return in_file, out_file,pt
    
    

def main():
    win = GraphWin("STUDENT DETAILS", 500,500)
    win.setCoords(0.0,0.0,5.0,5.0)
    b_gpa = Button(win, Point(1,1), 0.5, 0.5, "GPA")
    b_name = Button(win, Point(2.5,1), 0.5, 0.5, "NAME")
    b_hour = Button(win, Point(4,1), 0.5, 0.5, "HOUR")
    b_gpa.activate()
    b_name.activate()
    b_hour.activate()
    infiles,outfiles,pt = getInput(win)
    data = readFile(infiles)
    
    if b_gpa.clicked(pt):
            data.sort(key=Student.gpa, reverse=True)
        
    elif b_name.clicked(pt):
            data.sort(key=Student.get_name)
            
    elif b_hour.clicked(pt):
            data.sort(key=Student.get_hour)
            
    writeFile(data, outfiles)
    print("DONE!!!")
    
        
    
if __name__ == '__main__':
    main()
    
        
