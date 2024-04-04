from turtle import *

import turtle
turtle.Screen()
t = turtle.Turtle()
t.shape("arrow")
def kwadrat(color = 'black'):
    t.color(color)
    for x in range(5):
        t.forward(100)
        t.left(90)
    t.forward(100)
kwadrat()
kwadrat('red')
kwadrat('green')
kwadrat('blue')

t.hideturtle()
done()
