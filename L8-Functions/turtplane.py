from turtle import *

import turtle
turtle.Screen()
t = turtle.Turtle()
t.shape("arrow")
t.color("black")
t.speed(100)

begin_fill()
circle(150, 180)
color("DarkGreen")
circle(150, 180)
end_fill()
hideturtle()
t.up()
t.goto(-20, 300)
t.down()
t.color("grey")
t.left(90)
t.forward(30)
t.left(90)
t.forward(10)
t.left(-135)
t.forward(45)
t.color("black")
t.right(90)
t.forward(45)
t.right(135)
t.forward(10)
t.right(-90)
t.forward(30)
t.up()
t.goto(20, 0)
t.down()
t.color("black")
t.forward(30)
t.left(90)
t.forward(10)
t.left(-135)
t.forward(45)
t.color("gray")
t.right(90)
t.forward(45)
t.right(135)
t.forward(10)
t.right(-90)
t.forward(30)
t.hideturtle()
up()
showturtle()
goto(-550, 150)
color("DarkGoldenrod2")
down()
circle(55)
hideturtle()
done()