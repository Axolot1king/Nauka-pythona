from turtle import *

import turtle
turtle.Screen()
t = turtle.Turtle()
t.shape("arrow")
t.color('black')
for x in range(1, 5, 1):
    t.forward(100)
    t.left(90)
t.forward(100)
t.color("red")
for x in range(1, 5, 1):
    t.forward(100)
    t.left(90)
t.left(90)
t.forward(100)
t.color("blue")
for x in range(1, 5, 1):
    t.forward(100)
    t.left(90)
t.right(90)
t.color("green")
for x in range(1, 4, 1):
    t.forward(100)
    t.left(90)
t.hideturtle()
done()
