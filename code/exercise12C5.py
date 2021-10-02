import time
from graphics import *
class Display:
    def __init__(self):
        window = GraphWin("HIGH-SCORES", 500, 600)
        window.setBackground("green3")
        filename2 = "Highscore.txt"
        infile = open(filename2, "r")
        a = 30
        for line in infile.readlines():
            introduction = Text(Point(300, a), line)
            introduction.setFill("yellow2")
            introduction.setSize(10)
            introduction.setStyle("bold")
            introduction.draw(window)
            window.setBackground("green3")
            a = a + 30
        time.sleep(5)
        window.close()
