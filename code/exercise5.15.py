from tkinter.filedialog import askopenfilename
from graphics import *
def bar_chart():
    print("This program is to print the bar_chart of student scores")
    win = GraphWin("student score", 500,500)
    win.setCoords(0.0, 0.0, 12.0, 12.0)
    file_name = askopenfilename()
    file = open(file_name, "r")
    details1 = int(file.readline())
    details2 = file.readline().split()
    details3 = file.readline().split()
    y = 0
    k = 0
    for x in details2:
        y = y + 1
        Text(Point(2,9-y), x).draw(win)
    for i in details3:
        i = int(i)
        k = k + 1
        Rectangle(Point(3,9-k), Point((i/10)+3,9.5-k)).draw(win)
bar_chart()
