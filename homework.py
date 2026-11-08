# homework: in class, we drew one carrot inside our canvas
# TODO: by calling the draw_carrot() function, draw 10 carrots with random spawn positions inside the canvas.
# A hint has been given to you.
# website to run turtle is https://play.pyroom.app/playground

import turtle
import random

# ---------- Setup ----------
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0) # speed 0 is the fastest
t.pensize(1)
t.pencolor("green")
t.fillcolor("green")
screen.bgcolor("skyblue")
screen.setup(1000, 500)

# we are going to draw a beautiful garden today

# ground
t.goto(-500, 50)
t.begin_fill()
for i in range(4):
    t.forward(1000)
    t.right(90)
t.end_fill()

t.goto(0, 0)

# one carrot:
def draw_carrot():
    t.pencolor("black")
    t.fillcolor("orange")
    t.begin_fill()
    t.forward(30)
    t.right(100)
    t.forward(80)
    t.right(160)
    t.forward(80)
    t.end_fill()

    t.pensize(10)
    t.pencolor("lime")
    t.forward(30)
    t.forward(-30)
    t.setheading(0)
    t.forward(30)
    t.left(75)
    t.forward(30)
    t.setheading(0)
    t.pensize(1)

# hint: you'll need this function
def teleport(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

for i in range(10):
    teleport(random.randint(-500, 500), random.randint(-250, 250))
    draw_carrot()
screen.exitonclick()
