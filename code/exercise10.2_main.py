from drawface import DrawFace

def main():

    win = GraphWin("connonball Animation", 640,480, autoflush = False)
    win.setCoords(-10, -10, 210, 155)

    face = drawface(Point(2,3), 0.5)
    face.eye(2,3)
    face.nose(2,3)
    face.mouth(2,3)

   
    

main()
    
        
