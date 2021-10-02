from graphics import *
def main():
    win = GraphWin("colour changer", 500, 500)
    while True:
        key = win.getKey()
        if key=="q":
            break
        if key=="r":
            win.setBackground("pink")
        elif key=="b": 
            win.setBackground("lightblue")
        elif key=="w": 
            win.setBackground("white")
        elif key=="g": 
            win.setBackground("lightgrey")
    win.close()
main()
            
        
            
            
        
