"""
SUNFLOWER DRAWING FUNCTIONS
===========================
Phyllotactic sunflower motif for the center of the Pookalam.
"""

import math


def draw_sunflower_petal(turtle, x, y, length=10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.right(20)
    turtle.forward(length)
    turtle.left(40)
    turtle.forward(length)
    turtle.left(140)
    turtle.forward(length)
    turtle.left(40)
    turtle.forward(length)
    turtle.penup()
    turtle.end_fill()


def draw_phyllotactic_sunflower(turtle, total, petalstart, angle=137.508, cspread=1.35):
    turtle.hideturtle()
    turtle.speed(0)
    turtle.shape("circle")
    turtle.shapesize(0.11)
    phi = angle * (math.pi / 180.0)

    for n in range(total):
        r = cspread * math.sqrt(n)
        theta = n * phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)

        turtle.penup()
        turtle.setpos(x, y)
        turtle.pendown()
        turtle.setheading(n * angle)
        if n > petalstart - 1:
            draw_sunflower_petal(turtle, x, y)
        else:
            turtle.color("#3b1f0a")
            turtle.fillcolor("#6b3f16")
            turtle.stamp()
