from graphics import *
def handlekey(key, win):
    
    if key=="r":
        win.setBackground("pink")
    elif key=="b": 
        win.setBackground("lightblue")
    elif key=="w": 
        win.setBackground("white")
    elif key=="g": 
        win.setBackground("lightgrey")
def handlemouse(pt, win):
    pass
    
    
    
def main():
    win = GraphWin("color changing", 500, 500)
    while True:
       
        key = win.checkKey()
        if key=="q":
            break
        if key:  
            handlekey(key, win)
        
        pt = win.checkMouse()
        if pt:
            handlemouse(pt, win)
    win.close()
main()
    
    
