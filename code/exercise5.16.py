from tkinter.filedialog import askopenfilename
from graphics import *
def histogram():
    print("This program is to print the bar_chart of student scores")
    win = GraphWin("student score", 500,500)
    win.setCoords(-1.0, 0.0, 12.0, 12.0)
    file_name = askopenfilename()
    file = open(file_name, "r")
    details = file.readlines()
    acc = -1
    count_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in details:
        count_score[int(num)] += 1
    for x in range(0,11):
         Text(Point(x,2), x).draw(win)
    for i in count_score:
        acc = acc+1
        Rectangle(Point(acc-0.2,3), Point(acc+0.3, i+3)).draw(win)
        print(i)
        
       
        
histogram()
