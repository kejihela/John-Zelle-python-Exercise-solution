from graphics import *
win = GraphWin()
left_eye = Circle(Point(80,100), 10)
left_eye.setFill('yellow')
left_eye.setOutline('red')
left_eye.draw(win)

#right_eye = Circle(Point(130,100), 10)
#right_eye.setFill('yellow')
#right_eye.setOutline('red')
#right_eye.draw(win)

right_eye = left_eye.clone()
right_eye.move(40,0)
right_eye.draw(win)

