import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightgreen")

# Create a turtle for drawing
axolotl = turtle.Turtle()
axolotl.speed(0)  # Set the drawing speed to the fastest

# Function to draw a filled circle
def draw_circle(color, radius, x, y):
    axolotl.penup()
    axolotl.goto(x, y)
    axolotl.pendown()
    axolotl.color(color)
    axolotl.begin_fill()
    axolotl.circle(radius)
    axolotl.end_fill()

# Draw the axolotl's body
draw_circle("blue", 50, 0, -50)

# Draw the axolotl's eyes
draw_circle("white", 7, -20, 0)
draw_circle("white", 7, 20, 0)
draw_circle("black", 3, -20, 10)
draw_circle("black", 3, 20, 10)

# Draw the axolotl's smile
axolotl.penup()
axolotl.goto(-20, -10)
axolotl.pendown()
axolotl.width(2)
axolotl.setheading(-60)
axolotl.circle(25, 120)

# Draw the axolotl's crown
axolotl.penup()
axolotl.goto(-50, 40)
axolotl.pendown()
axolotl.color("gold")
axolotl.begin_fill()
axolotl.setheading(60)
for _ in range(3):
    axolotl.forward(100)
    axolotl.right(120)
axolotl.end_fill()

# Hide the turtle
axolotl.hideturtle()

# Keep the window open
turtle.done()
