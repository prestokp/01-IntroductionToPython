"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Kirk Preston.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.SimpleTurtle()
size = 400
rg.SimpleTurtle()
falcon=rg.SimpleTurtle('turtle')
falcon.pen = rg.Pen('orange', 20)
for k in range(5):
    falcon.speed = 100
    falcon.draw_circle(100)
    falcon.right(45)
    falcon.forward(10)
    falcon.left(45)
    falcon.forward(10)
size = size - 20

rg.SimpleTurtle('turtle')
dragon=rg.SimpleTurtle('turtle')
dragon.Pen = rg.Pen('turtle', 10)
for k in range(5):
    dragon.draw_regular_polygon(6, 30)
    dragon.speed = falcon.speed
    dragon.right(10)
    dragon.forward(10)
    dragon.left(10)
    dragon.forward(10)
    size = size - 20

window = rg.TurtleWindow()
window.close_on_mouse_click()

