# importing required modules
import turtle
from turtle import *
# penspeed 100
speed(100)
# pencolor cyan
color('cyan')
# background color black
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
turtle.mainloop()
