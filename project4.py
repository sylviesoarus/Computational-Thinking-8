import turtle, time, random
from utils import *

# Section 1 - setup
set_background("pasta")
# the goal is to make as many meatballs and cheese as possible
# TODO - create at least two variables and set their starting value. ex: cookies = 0
cheese = 0
meatball = 0


# Section 2 - controls
def make_meatball ():
    global meatball
    meatball += 1
    x = random.randint (-300,300)
    y = random. randint (-300, 300)
    create_sprite ("meatball",x,y)
window.onkeypress(make_meatball,"space")
#when space is pressed, a meatball appers on the screen
def add_cheese ():
    global cheese
    cheese += 1
    x = random.randint (-300,300)
    y = random. randint (-300,300)
    create_sprite ("cheese",x,y)
window.onkeypress (add_cheese, "g")
# when g is pressed, a parmesean cheese apears on the screen



# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()