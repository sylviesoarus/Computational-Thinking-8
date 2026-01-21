import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 200
x2 = -300
y2 = 50
x3 = -300
y3 = -100
x4 = -300
y4 = -250


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("park")
t1 = create_sprite("cool_dog",x1,y1)
t2 = create_sprite("cat2",x2,y2)
t3 = create_sprite("corgi.gif",x3,y3)
t4 = create_sprite("dog",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(35):
    x1 +=56
    x2 +=45
    x3 +=32
    x4 +=20

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.8)
# the cool dog will always win because its speed is set higher then the rest.

# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Cool dog Won!")
elif x2 >= x1 and x2>= x3 and x2 >= x4:
    print("the Cat won!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print ("The corgi Won")
elif x4 >= x3 and x4>= x2 and x4 >= x1:
    print ("the Dog won!")


turtle.exitonclick()