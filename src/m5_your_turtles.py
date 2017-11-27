"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Victoria May Szalay.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

Colleen = rg.SimpleTurtle('turtle')
Colleen.pen = rg.Pen('yellow', 3)
Colleen.speed = 10
Andrew = rg.SimpleTurtle('turtle')
Andrew.pen = rg.Pen('green',3)
Andrew.speed = 10
Jade = rg.SimpleTurtle('turtle')
Jade.pen = rg.Pen('red',3)
Jade.speed = 10
Will = rg.SimpleTurtle('turtle')
Will.pen = rg.Pen('yellow',3)
Will.speed = 10
size = 200

for k in range(7):
    Colleen.draw_square(size)

    Colleen.pen_up()
    Colleen.right(45)
    Colleen.forward(10)
    Colleen.left(45)

    Colleen.pen_down()
    size = size - 12

for k in range(7):
    Andrew.draw_circle(size)

    Andrew.pen_up()
    Andrew.right(45)
    Andrew.forward(10)
    Andrew.left(45)

    Andrew.pen_down()
    size = size -12

for k in range(7):
    Jade.draw_regular_polygon(8,size)

    Jade.pen_up()
    Jade.right(45)
    Jade.forward(10)
    Jade.left(45)

    Jade.pen_down()
    size=size-12

window.close_on_mouse_click()