import turtle, math, time, random
from utils import *
#the goal of the game is to get to the end with out dying
s1 = create_sprite("marshmallow", -300,-100)
set_background("campground")
f1 = create_sprite("fire")

sprite_list = []
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

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress (move_left, "Left")
window.onkeypress (move_right,"Right")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    # TODO - add code for automatic actions
    if i % 50==0:
         x= random.randint (-350, 350)
         y=350
         f1 = create_sprite("fire", x,y)
         sprite_list.append(f1)

    for f1 in sprite_list:
         x= f1.xcor()
         y=f1 .ycor()-5
         f1.goto(x, y)

    for fire in sprite_list:
        if get_distance(s1, fire ) <100:
            s1.goto(-300,0)
            fire.hideturtle()
            sprite_list.remove(fire)




    # TODO - make an if statement for ending the game

    if s1.xcor() >300:
        print ("YOU WON GAME OVER") 
        break 
    
    time.sleep(0.01)
    window.update()



	
print("Game Over")