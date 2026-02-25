import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)
s2 = create_sprite("cool_dog",0,-100)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 7
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 7
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 7
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 7
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress (move_left, "a")
window.onkeypress (move_right,"d")
# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")




def move_up():
    x = s2.xcor()
    y = s2.ycor() + 7
    s2.goto(x,y)
        
def move_down():
    x = s2.xcor()
    y = s2.ycor() - 7
    s2.goto(x,y)
    
def move_left():
    x = s2.xcor() - 7
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right(): 
    x = s2.xcor() + 7
    y = s2.ycor() 
    s2.goto(x,y)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress (move_left, "Left")
window.onkeypress (move_right,"Right")
# Section 3: define other controls
def draw ():
    s1.pendown()
window.onkeypress (draw,"c")

def stop_drawing():
    s1.penup()
window.onkeypress(stop_drawing,"f")

def erase():
    s1.clear()

def red_pen():
    s1.color ("red")

def green_pen ():
    s1.color("green")

def reset ():
    s1.goto(0,0)

# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()