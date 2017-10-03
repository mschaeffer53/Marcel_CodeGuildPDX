'''
Lab 1: drawing a stick figure using turtle
Marcel Schaeffer
10/3/2017
'''

from turtle import *

#draw head
circle(50)

#draw neck and arms
left(270)
forward(50)
left(90)
forward(50)
backward(100)
forward(50)

#draw legs
left(90)
backward(50)
setheading(225)
forward(50)
backward(50)
setheading(315)
forward(50)

#draw eyes
penup()
home()
left(65)
forward(60)
pendown()
dot()

penup()
home()
right(250)
forward(60)
pendown()
dot()





"""

fillcolor('green')

begin_fill()

x = 100
y = 144



forward(x)
left(y)
forward(x)
left(y)
forward(x)
left(y)
forward(x)
left(y)

end_fill()

"""
done()
