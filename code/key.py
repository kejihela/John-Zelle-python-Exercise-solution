from graphics import *
def text_handling():
    win = GraphWin("Text handling", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)
text_handling()

    
