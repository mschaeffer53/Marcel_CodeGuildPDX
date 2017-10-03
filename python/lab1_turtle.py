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
pendown()
dot()
forward(10)



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
